# import google.generativeai as genai
# import time

# # Configure the API key
# genai.configure(api_key="AIzaSyBSfTkOjze54CPY7RwyfzWoUJb1gfV-Gdk")

# # Initialize the model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Define the prompts
# prompts = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

# # Function to handle API calls with retry mechanism
# def call_with_retry(prompt, model, max_retries=25):
#     retry_count = 0
#     timer_started = False
#     timer_start = None

#     while retry_count < max_retries:
#         try:
#             # Try to generate a response
#             response = model.generate_content(prompt)
#             if timer_started:
#                 # Stop the timer if API is responding again
#                 timer_elapsed = time.time() - timer_start
#                 print(f"API is responding again! Downtime: {timer_elapsed:.2f} seconds.")
#                 timer_started = False  # Reset the timer state
#             return response.text.strip()

#         except Exception as e:
#             # Check for rate limit error (429)
#             if "429" in str(e):
#                 if not timer_started:
#                     # Start the timer if not already started
#                     timer_started = True
#                     timer_start = time.time()
#                 print("Rate limit exceeded. Retrying...")
#                 time.sleep(5)  # Wait for 5 seconds before retrying
#             else:
#                 # For other exceptions, re-raise the error
#                 raise e

#     # If all retries are exhausted
#     raise RuntimeError("Max retries exceeded. API is still unavailable.")

# # Iterate through prompts
# for i, prompt in enumerate(prompts):
#     try:
#         response = call_with_retry(prompt, model)
#         print(f"Response {i+1}: {response}")
#     except Exception as e:
#         print(f"Error on prompt {i+1}: {e}")
