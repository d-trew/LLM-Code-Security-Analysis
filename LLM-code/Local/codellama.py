import os
import json
import requests
import time
from datetime import datetime
from typing import List, Dict, Set

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codellama:7b-instruct-q4_0"
DATASET_PATH = os.path.join(os.getcwd(), "GCJ", "2016-2022_extracted_prompts_clean.json")
OUTPUT_DIR = os.path.join(os.getcwd(), "LLM_Responses")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "codellama_responses.json")

# Optimized settings
REQUESTS_PER_MINUTE = 30  # Reduced for stability
MIN_INTERVAL = 60 / REQUESTS_PER_MINUTE
MAX_RETRIES = 3  # Reduced retries to fail faster for debugging

def setup_environment():
    """Ensure output directory exists."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data() -> tuple[List[Dict], Set[str]]:
    """Load prompts and check which ones have been processed."""
    try:
        with open(DATASET_PATH, 'r') as f:
            prompts = json.load(f)
    except Exception as e:
        print(f"Error loading prompts: {str(e)}")
        raise
    
    processed = set()
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f:
                existing_results = json.load(f)
                processed = {(r['source'], r['problem_name']) for r in existing_results}
        except Exception as e:
            print(f"Warning: Could not load existing results: {str(e)}")
    
    return prompts, processed

def generate_code(prompt_text: str) -> str:
    """Generate code with enhanced error handling."""
    prompt = f"""Write a Python program based on this description.
Return ONLY the Python code with no additional explanation or formatting.

Description:
{prompt_text}"""
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "options": {
            "temperature": 0.5,
            "num_ctx": 4096,
            "num_gpu": 35,
            "repeat_penalty": 1.1
        },
        "stream": False  # Explicitly disable streaming
    }
    
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json=payload,
            timeout=120
        )
        
        # Debugging output
        print(f"API Response Status: {response.status_code}")
        if response.status_code != 200:
            print(f"API Response Content: {response.text}")
        
        response.raise_for_status()
        result = response.json()
        
        if "response" not in result:
            raise ValueError("No 'response' field in API output")
            
        code = result["response"].strip()
        
        # Clean the output
        for marker in ["```python", "```", "<s>", "</s>"]:
            code = code.replace(marker, "")
        return code.strip()
        
    except Exception as e:
        print(f"Generation error details: {str(e)}")
        if 'response' in locals():
            print(f"Full response: {response.text}")
        raise RuntimeError(f"Generation failed: {str(e)}")

def process_prompts():
    """Main processing loop with enhanced debugging."""
    setup_environment()
    prompts, processed = load_data()
    
    # Initialize results
    results = []
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f:
                results = json.load(f)
        except Exception as e:
            print(f"Warning: Could not load existing results: {str(e)}")
    
    total_prompts = len(prompts)
    start_time = time.time()
    failures = []
    
    print(f"\nStarting CodeLlama processing of {total_prompts} prompts")
    print(f"Already processed: {len(processed)}")
    print(f"Remaining: {total_prompts - len(processed)}\n")
    
    for i, prompt in enumerate(prompts, 1):
        prompt_id = (prompt['source'], prompt['problem_name'])
        if prompt_id in processed:
            continue
            
        print(f"\nProcessing [{i}/{total_prompts}] {prompt['problem_name']}")
        
        for attempt in range(MAX_RETRIES):
            try:
                print(f"Attempt {attempt + 1} of {MAX_RETRIES}")
                start = time.time()
                code = generate_code(prompt['problem_statement'])
                gen_time = time.time() - start
                
                results.append({
                    "source": prompt['source'],
                    "problem_name": prompt['problem_name'],
                    "python_code": code,
                    "generated_at": datetime.now().isoformat(),
                    "generation_time": gen_time,
                    "model": MODEL_NAME
                })
                
                # Save after each success
                with open(OUTPUT_FILE, 'w') as f:
                    json.dump(results, f, indent=2)
                
                print(f"Successfully generated in {gen_time:.1f}s")
                break
                
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == MAX_RETRIES - 1:
                    failures.append({
                        "source": prompt['source'],
                        "problem_name": prompt['problem_name'],
                        "error": str(e),
                        "attempts": attempt + 1
                    })
                time.sleep(2 ** attempt)  # Exponential backoff
        else:
            print(f"All attempts failed for {prompt['problem_name']}")
            continue
            
        # Rate limiting
        elapsed = time.time() - start_time
        expected_time = i * MIN_INTERVAL
        if elapsed < expected_time:
            sleep_time = max(0, expected_time - elapsed)
            print(f"Waiting {sleep_time:.1f}s for rate limiting")
            time.sleep(sleep_time)
    
    # Final report
    success_count = len(results) - (len([r for r in results if (r['source'], r['problem_name']) in processed]))
    print(f"\n{'='*50}")
    print(f"Processing Complete!")
    print(f"Total prompts: {total_prompts}")
    print(f"Successfully processed: {success_count}")
    print(f"Failures: {len(failures)}")
    print(f"Total time: {time.time() - start_time:.1f} seconds")
    
    if failures:
        print("\nFailed Prompts:")
        for i, fail in enumerate(failures, 1):
            print(f"{i}. {fail['problem_name']}")
            print(f"   Error: {fail['error']}")
            print("-" * 50)

if __name__ == "__main__":
    try:
        # Verify connection and model
        print("Checking Ollama server...")
        health = requests.get("http://localhost:11434", timeout=5)
        health.raise_for_status()
        
        print("Checking model availability...")
        models = requests.get("http://localhost:11434/api/tags", timeout=5).json()
        if not any(m["name"].startswith("codellama") for m in models.get("models", [])):
            print("Error: CodeLlama model not found. Please run:")
            print("ollama pull codellama:7b-instruct-q4_0")
            exit(1)
            
        print("Starting processing...")
        process_prompts()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
