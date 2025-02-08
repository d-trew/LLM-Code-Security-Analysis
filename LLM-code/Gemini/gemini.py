import os
import json
import google.generativeai as genai
import time

# Configure the API key
genai.configure(api_key="AIzaSyBSfTkOjze54CPY7RwyfzWoUJb1gfV-Gdk")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Load the dataset
dataset_path = os.path.join(os.getcwd(), "GCJ", "2016-2022_extracted_prompts_clean.json")
with open(dataset_path, 'r', encoding='utf-8') as file:
    prompts = json.load(file)

# Rate limiting parameters
REQUESTS_PER_MINUTE = 15
TOKENS_PER_MINUTE = 1000000
REQUESTS_PER_DAY = 1500

# Track usage
request_count = 0
token_count = 0
start_time = time.time()

# Output file to save responses
output_file = os.path.join(os.getcwd(), "LLM", "LLM_responses", "gemini_responses.json")

# Load existing responses if the file exists
if os.path.exists(output_file):
    with open(output_file, 'r', encoding='utf-8') as file:
        results = json.load(file)
else:
    results = []

# List to store failed prompts (due to finish_reason 4 or other errors)
failed_prompts = []

# Function to handle API calls with retry mechanism
def call_with_retry(prompt, model, max_retries=3):
    global request_count, token_count, start_time

    retry_count = 0
    while retry_count < max_retries:
        try:
            # Check rate limits
            if request_count >= REQUESTS_PER_MINUTE or token_count >= TOKENS_PER_MINUTE:
                print("Rate limit exceeded. Checking API availability every 5 seconds...")
                wait_for_api_availability()
                request_count = 0
                token_count = 0
                start_time = time.time()

            if request_count >= REQUESTS_PER_DAY:
                raise Exception("Daily request limit reached.")

            # Try to generate a response
            response = model.generate_content(prompt)

            # Check if the response is valid
            if response.candidates and response.candidates[0].finish_reason == 1:  # Finish reason 1 = valid response
                request_count += 1
                token_count += len(response.text.split())  # Approximate token count
                return response.text.strip()
            elif response.candidates and response.candidates[0].finish_reason == 4:  # Finish reason 4 = copyrighted material
                raise Exception("Invalid response: finish_reason = 4 (copyrighted material)")
            else:
                raise Exception(f"Invalid response: finish_reason = {response.candidates[0].finish_reason}")

        except Exception as e:
            if "429" in str(e):  # Rate limit error
                print(f"Rate limit exceeded: {e}. Retrying...")
                time.sleep(5)  # Wait before retrying
            else:  # Other errors (e.g., finish_reason 4)
                raise e

    raise RuntimeError("Max retries exceeded. API is still unavailable.")

# Function to wait for API availability
def wait_for_api_availability():
    print("Waiting for API to become available...")
    start_wait_time = time.time()
    while True:
        try:
            # Use the next prompt in the JSON file to check API availability
            if prompts:
                next_prompt = prompts[0]["problem_statement"]
                response = model.generate_content(next_prompt)
                if response.candidates and response.candidates[0].finish_reason == 1:
                    elapsed_time = time.time() - start_wait_time
                    print(f"API is available again! Downtime: {elapsed_time:.2f} seconds.")
                    return
        except Exception as e:
            print(f"API still unavailable: {e}. Checking again in 5 seconds...")
            time.sleep(5)

# Process each prompt
for prompt in prompts:
    try:
        # Skip if already processed
        if any(result["source"] == prompt["source"] for result in results):
            print(f"Skipping already processed: {prompt['problem_name']}")
            continue

        # Construct the prompt for Gemini
        gemini_prompt = f"Write a Python program and ONLY return python code with the description: {prompt['problem_statement']}"

        # Send the prompt to Gemini and get the response
        python_code = call_with_retry(gemini_prompt, model)

        # Save the response with the source
        result = {
            "source": prompt["source"],
            "problem_name": prompt["problem_name"],
            "python_code": python_code
        }
        results.append(result)

        # Save the results to the JSON file after each prompt
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(results, file, indent=4)

        print(f"Processed: {prompt['problem_name']}")

    except Exception as e:
        if "finish_reason = 4" in str(e):  # Copyrighted material error
            print(f"Prompt failed due to copyrighted material: {prompt['problem_name']}. Moving on.")
            failed_prompts.append(prompt)  # Add to failed prompts list
        else:  # Other errors
            print(f"Prompt failed: {prompt['problem_name']}. Error: {e}")
            failed_prompts.append(prompt)  # Add to failed prompts list

# Retry failed prompts after re-establishing API connection
if failed_prompts:
    print("Re-establishing API connection and retrying failed prompts...")
    wait_for_api_availability()

    for prompt in failed_prompts:
        try:
            # Construct the prompt for Gemini
            gemini_prompt = f"Write a Python program and ONLY return python code with the description: {prompt['problem_statement']}"

            # Send the prompt to Gemini and get the response
            python_code = call_with_retry(gemini_prompt, model)

            # Save the response with the source
            result = {
                "source": prompt["source"],
                "problem_name": prompt["problem_name"],
                "python_code": python_code
            }
            results.append(result)

            # Save the results to the JSON file after each prompt
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(results, file, indent=4)

            print(f"Processed (retry): {prompt['problem_name']}")

        except Exception as e:
            print(f"Error processing (retry) {prompt['problem_name']}: {e}")

print("Processing complete. Responses saved to gemini_responses.json.")