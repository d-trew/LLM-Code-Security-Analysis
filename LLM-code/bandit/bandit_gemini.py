import subprocess
import os
import json

# Directory containing the Python files
python_files_dir = "LLM_Responses/responses_into_files/gemini"

# Output directory for Bandit reports
output_dir = "LLM_Responses/bandit_reports\gemini"
os.makedirs(output_dir, exist_ok=True)

# Iterate over all Python files in the directory
for root, _, files in os.walk(python_files_dir):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            report_path = os.path.join(output_dir, f"{file}_bandit_report.json")
            report_path = report_path.replace(".py", "")
            # Run Bandit on the file
            print(f"Running Bandit on {file_path}...")
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