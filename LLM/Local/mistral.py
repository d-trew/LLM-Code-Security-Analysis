import os
import json
import requests
import time
from urllib.parse import urljoin

# Ollama configuration
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "mistral"

# Load the dataset
dataset_path = os.path.join(os.getcwd(), "GCJ", "2016-2022_extracted_prompts_clean.json")
with open(dataset_path, 'r', encoding='utf-8') as file:
    prompts = json.load(file)

# Output file
output_file = os.path.join(os.getcwd(), "LLM", "LLM_responses", "mistral_responses.json")

# Load existing responses
if os.path.exists(output_file):
    with open(output_file, 'r', encoding='utf-8') as file:
        results = json.load(file)
else:
    results = []

failed_prompts = []

def call_with_retry(prompt, prompt_name, max_retries=3):
    for retry in range(max_retries):
        try:
            print(f"\n=== Processing prompt: {prompt_name} ===")
            print(f"Attempt {retry + 1}/{max_retries}")
            print("Constructing API request...")
            
            mistral_prompt = (
                "Write a complete Python program based on this description. "
                "Return ONLY the raw Python code with no explanations:\n\n"
                f"{prompt}"
            )

            print("Sending to Ollama API...")
            start_time = time.time()
            response = requests.post(
                urljoin(OLLAMA_BASE_URL, "/api/generate"),
                json={
                    "model": MODEL_NAME,
                    "prompt": mistral_prompt,
                    "stream": False,
                    "options": {"temperature": 0.7, "num_predict": 2000}
                },
                timeout=60
            )
            elapsed = time.time() - start_time
            print(f"API call completed in {elapsed:.2f}s with status: {response.status_code}")

            if response.status_code == 200:
                response_data = response.json()
                print("API response received successfully")
                code = extract_python_code(response_data["response"])
                print("Code extraction complete")
                return code
            else:
                print(f"API error response: {response.text}")
                raise Exception(f"Status {response.status_code}")

        except Exception as e:
            print(f"Attempt {retry + 1} failed: {str(e)}")
            if retry < max_retries - 1:
                print("Waiting 2 seconds before retry...")
                time.sleep(2)
    
    print(f"All {max_retries} attempts failed for this prompt")
    return None

def extract_python_code(text):
    if "```python" in text:
        code = text.split("```python")[1].split("```")[0]
    elif "```" in text:
        code = text.split("```")[1].split("```")[0]
    else:
        code = text
    return code.strip()

# Process each prompt
for i, prompt in enumerate(prompts):
    print(f"\n\n=== Starting prompt {i + 1}/{len(prompts)} ===")
    print(f"Problem: {prompt['problem_name']}")
    
    if any(result["source"] == prompt["source"] for result in results):
        print("Already processed - skipping")
        continue

    python_code = call_with_retry(prompt['problem_statement'], prompt['problem_name'])
    
    if python_code:
        results.append({
            "source": prompt["source"],
            "problem_name": prompt["problem_name"],
            "python_code": python_code
        })
        
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(results, file, indent=4)
        print("Successfully saved response")
    else:
        failed_prompts.append(prompt)
        print("Added to failed prompts list")

print("\n=== Processing Complete ===")
print(f"Successfully processed {len(results)} prompts")
print(f"Failed to process {len(failed_prompts)} prompts")

if failed_prompts:
    print("\n=== Retrying Failed Prompts ===")
    for prompt in failed_prompts:
        print(f"\nRetrying: {prompt['problem_name']}")
        python_code = call_with_retry(prompt['problem_statement'], prompt['problem_name'])
        
        if python_code:
            results.append({
                "source": prompt["source"],
                "problem_name": prompt["problem_name"],
                "python_code": python_code
            })
            
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(results, file, indent=4)
            print("Successfully saved retry response")

print("\nFinal results saved to:", output_file)