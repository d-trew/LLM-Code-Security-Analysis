import json
import os

GEMINI_RESPONSES_JSON_PATH = "LLM_Responses/codegemma_responses.json"
TARGET_DIR = "LLM_Responses/responses_into_files/codegemma"

# Ensure the target directory exists
os.makedirs(TARGET_DIR, exist_ok=True)

# Load the JSON file
with open(GEMINI_RESPONSES_JSON_PATH, 'r') as f:
    data = json.load(f)

# Extract Python code from each entry
for entry in data:
    problem_name = entry.get('problem_name', 'unnamed_problem')  # Default name if missing
    python_code: str = entry.get('python_code', '')
    python_code = python_code.replace("```python", "").replace("```", "").strip()
    # Sanitize problem_name to remove invalid characters
    problem_name = problem_name.replace("?", "").replace(":", "")
    
    # Skip if python_code is empty
    if not python_code.strip():
        print(f"Skipping {problem_name}: No Python code found.")
        continue
    
    # Write the code to a file
    file_path = os.path.join(TARGET_DIR, f"{problem_name}.py")
    try:
        with open(file_path, 'w', encoding='utf-8') as code_file:
            code_file.write(python_code)
        print(f"Successfully wrote {file_path}")
    except Exception as e:
        print(f"Failed to write {file_path}: {e}")