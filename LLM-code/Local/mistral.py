import os
import json
import requests
import time
from datetime import datetime
from typing import List, Dict, Set

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral" 
DATASET_PATH = os.path.join(os.getcwd(), "GCJ", "2016-2022_extracted_prompts_clean.json")
OUTPUT_DIR = os.path.join(os.getcwd(), "LLM_Responses") 
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mistral_responses.json")  # Changed filename

# Mistral-specific parameters (optimized for 7B model)
REQUESTS_PER_MINUTE = 40  # Higher throughput possible with Mistral
MIN_INTERVAL = 60 / REQUESTS_PER_MINUTE
MAX_RETRIES = 5  # Increased retries for stability

def setup_environment():
    """Ensure output directory exists."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data() -> tuple[List[Dict], Set[str]]:
    """Load prompts and check which ones have been processed."""
    with open(DATASET_PATH, 'r') as f:
        prompts = json.load(f)
    
    processed = set()
    
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            existing_results = json.load(f)
            # Create a set of (source, problem_name) tuples that have been processed
            processed = {(r['source'], r['problem_name']) for r in existing_results}
    
    return prompts, processed

def generate_code(prompt_text: str) -> str:
    """Generate code with Mistral-specific formatting."""
    prompt = f"""<s>[INST] Write a Python program based on this description.
Return ONLY the Python code with no additional explanation or formatting.

Description:
{prompt_text} [/INST]</s>"""
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "options": {
            "temperature": 0.5,
            "num_ctx": 8192,
            "num_gpu": 50
        }
    }
    
    response = requests.post(OLLAMA_API_URL, json=payload, timeout=180)
    response.raise_for_status()
    return response.json()["response"].strip()

def process_prompts():
    """Main processing loop with accurate progress tracking."""
    setup_environment()
    prompts, processed = load_data()
    
    # Load existing results or create new list
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            results = json.load(f)
    else:
        results = []
    
    total_prompts = len(prompts)
    start_time = time.time()
    success_count = 0
    failures = []
    
    print(f"\nStarting processing of {total_prompts} prompts")
    print(f"Already processed: {len(processed)}")
    print(f"Remaining: {total_prompts - len(processed)}\n")
    
    for i, prompt in enumerate(prompts, 1):
        # Check if this specific prompt has been processed
        prompt_id = (prompt['source'], prompt['problem_name'])
        if prompt_id in processed:
            continue
            
        try:
            start = time.time()
            code = generate_code(prompt['problem_statement'])
            gen_time = time.time() - start
            
            results.append({
                "source": prompt['source'],
                "problem_name": prompt['problem_name'],
                "python_code": code,
                "generated_at": datetime.now().isoformat(),
                "generation_time": gen_time
            })
            
            success_count += 1
            
            # Save progress after each successful generation
            with open(OUTPUT_FILE, 'w') as f:
                json.dump(results, f, indent=2)
                
            print(f"✅ [{i}/{total_prompts}] {prompt['problem_name']} ({gen_time:.1f}s)")
            
        except Exception as e:
            failures.append({
                "source": prompt['source'],
                "problem_name": prompt['problem_name'],
                "error": str(e)
            })
            
            print(f"❌ [{i}/{total_prompts}] Failed: {prompt['problem_name']}")
            
        finally:
            # Rate limiting
            elapsed = time.time() - start_time
            expected_time = i * MIN_INTERVAL
            if elapsed < expected_time:
                time.sleep(max(0, expected_time - elapsed))
    
    # Final report
    print(f"\n{'='*50}")
    print(f"Processing complete!")
    print(f"Total prompts: {total_prompts}")
    print(f"Successfully processed: {success_count}")
    print(f"Failures: {len(failures)}")
    print(f"Total time: {time.time() - start_time:.1f} seconds")
    
    # Print failures at the end
    if failures:
        print("\nFailed Prompts:")
        for i, failure in enumerate(failures, 1):
            print(f"{i}. {failure['problem_name']} (Source: {failure['source']})")
            print(f"   Error: {failure['error']}")
            print("-" * 50)

if __name__ == "__main__":
    try:
        process_prompts()
    except KeyboardInterrupt:
        print("\nProcess interrupted. Current progress has been saved.")
    except Exception as e:
        print(f"\nFatal error: {str(e)}")