import os
import json
import requests
import time
from datetime import datetime
from typing import List, Dict

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b-instruct-q4_0"  # Your local model
DATASET_PATH = os.path.join(os.getcwd(), "GCJ", "2016-2022_extracted_prompts_clean.json")
OUTPUT_DIR = os.path.join(os.getcwd(), "LLM_Responses")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "llama_responses.json")

# Rate limiting (adjust based on your GPU capacity)
REQUESTS_PER_MINUTE = 30
MIN_INTERVAL = 60 / REQUESTS_PER_MINUTE  # Seconds between requests

def ensure_output_dir():
    """Create output directory if it doesn't exist."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_prompts() -> List[Dict]:
    """Load prompts from JSON file."""
    print(f"Loading prompts from {DATASET_PATH}")
    with open(DATASET_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_existing_results() -> List[Dict]:
    """Load existing results if output file exists."""
    if os.path.exists(OUTPUT_FILE):
        print(f"🔍 Found existing results at {OUTPUT_FILE}")
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    print("🆕 No existing results found, starting fresh")
    return []

def generate_code(prompt_text: str, attempt: int = 1) -> str:
    """Generate Python code using local Llama model."""
    prompt = f"""Write a Python program based on this description.
Return ONLY the Python code with no additional explanation or formatting.

Description:
{prompt_text}"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.5,
            "top_p": 0.9,
            "num_ctx": 4096
        }
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        
        if "response" not in result:
            raise ValueError("No response in API output")
            
        return result["response"].strip()
    except Exception as e:
        if attempt <= 3:
            print(f"⚠Attempt {attempt} failed, retrying... (Error: {str(e)})")
            time.sleep(5 * attempt)  # Exponential backoff
            return generate_code(prompt_text, attempt + 1)
        raise RuntimeError(f"Failed after 3 attempts: {str(e)}")

def print_progress(current: int, total: int, start_time: float):
    """Print a progress bar with time estimation."""
    elapsed = time.time() - start_time
    percent = (current / total) * 100
    eta = (elapsed / current) * (total - current) if current > 0 else 0
    
    progress_bar = f"[{'=' * int(percent//5):<20}] {percent:.1f}%"
    time_info = f"Elapsed: {elapsed:.0f}s | ETA: {eta:.0f}s"
    print(f"\r🔄 {progress_bar} | {time_info} | {current}/{total}", end="")

def process_prompts():
    """Main processing function with enhanced logging."""
    ensure_output_dir()
    prompts = load_prompts()
    results = load_existing_results()
    processed_sources = {r["source"] for r in results}
    failed_prompts = []
    
    total_prompts = len(prompts)
    processed_count = len(processed_sources)
    start_time = time.time()
    
    print(f"\nStarting processing of {total_prompts} prompts")
    print(f"Using model: {MODEL_NAME}")
    print(f"Saving results to: {OUTPUT_FILE}\n")

    for i, prompt in enumerate(prompts, 1):
        try:
            # Skip already processed
            if prompt["source"] in processed_sources:
                print_progress(i, total_prompts, start_time)
                continue

            # Print current task
            print(f"\n\nProcessing [{i}/{total_prompts}]: {prompt['problem_name']}")
            print(f"Source: {prompt['source']}")
            
            # Generate code with timing
            gen_start = time.time()
            python_code = generate_code(prompt["problem_statement"])
            gen_time = time.time() - gen_start
            
            # Save result
            results.append({
                "source": prompt["source"],
                "problem_name": prompt["problem_name"],
                "python_code": python_code,
                "generated_at": datetime.now().isoformat(),
                "generation_time": gen_time
            })

            # Save incrementally
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
                json.dump(results, file, indent=4)

            # Print success
            print(f"Generated in {gen_time:.1f}s")
            print(f"Code length: {len(python_code)} characters")
            
            # Rate limiting
            elapsed = time.time() - start_time
            print_progress(i, total_prompts, start_time)
            if elapsed < MIN_INTERVAL * i:
                time.sleep(max(0, MIN_INTERVAL * i - elapsed))

        except Exception as e:
            print(f"\nFailed: {prompt['problem_name']} - {str(e)}")
            failed_prompts.append(prompt)
            # Save progress even after failures
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
                json.dump(results, file, indent=4)

    # Final status report
    success_count = len(results) - len(processed_sources)
    failure_count = len(failed_prompts)
    
    print(f"\n\n{'='*50}")
    print(f"Processing complete!")
    print(f"Success: {success_count}")
    print(f"Failures: {failure_count}")
    print(f"Total time: {time.time() - start_time:.1f} seconds")
    print(f"Results saved to: {OUTPUT_FILE}")
    print(f"{'='*50}\n")

    # Retry failed prompts if any
    if failed_prompts:
        print(f"Attempting to retry {len(failed_prompts)} failed prompts...")
        retry_start = time.time()
        
        for prompt in failed_prompts:
            try:
                print(f"\nRetrying: {prompt['problem_name']}")
                python_code = generate_code(prompt["problem_statement"])
                
                results.append({
                    "source": prompt["source"],
                    "problem_name": prompt["problem_name"],
                    "python_code": python_code,
                    "generated_at": datetime.now().isoformat(),
                    "generation_time": time.time() - retry_start
                })
                
                print(f"Retry successful!")
                
                # Save after each retry
                with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
                    json.dump(results, file, indent=4)
                    
            except Exception as e:
                print(f"Retry failed: {str(e)}")

        print(f"\n🔚 Retry attempts completed in {time.time() - retry_start:.1f}s")

if __name__ == "__main__":
    # Verify Ollama is running
    try:
        print("Checking Ollama connection...")
        health_check = requests.get("http://localhost:11434", timeout=10)
        health_check.raise_for_status()
        print("Ollama server is ready!")
    except Exception as e:
        print("Error: Ollama server not running. Start it first with:")
        print("cd /scratch/dt00561/ollama/bin && ./ollama serve")
        exit(1)

    process_prompts()
