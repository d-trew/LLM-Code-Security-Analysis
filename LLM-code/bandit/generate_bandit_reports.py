import subprocess
import os
import json

# Base directories
responses_base_dir = "LLM_Responses/responses_into_files"
reports_base_dir = "LLM_Responses/bandit_reports"


# Iterate over each LLM directory in the responses directory
for llm_dir in os.listdir(responses_base_dir):
    response_dir = os.path.join(responses_base_dir, llm_dir)
    
    # Skip if not a directory
    if not os.path.isdir(response_dir):
        continue
    
    # Create corresponding report directory
    report_dir = os.path.join(reports_base_dir, llm_dir)
    os.makedirs(report_dir, exist_ok=True)
    
    print(f"\nProcessing LLM: {llm_dir}")
    print(f"Response directory: {response_dir}")
    print(f"Report directory: {report_dir}")
    
    # Process each Python file in the LLM's response directory
    for root, _, files in os.walk(response_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                # Create report filename (remove .py and add _bandit_report.json)
                report_filename = f"{os.path.splitext(file)[0]}_bandit_report.json"
                report_path = os.path.join(report_dir, report_filename)
                
                # Run Bandit on the file
                print(f"\nRunning Bandit on {file_path}...")
                result = subprocess.run(
                    ["bandit", "-f", "json", "-o", report_path, file_path],
                    capture_output=True,
                    text=True,
                )

                # Check if Bandit ran successfully
                if result.returncode == 0:
                    print(f"Bandit report saved to {report_path}")
                else:
                    print(f"Bandit failed to analyze {file_path}: {result.stderr}")