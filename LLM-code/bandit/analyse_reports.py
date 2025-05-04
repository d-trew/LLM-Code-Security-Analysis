import json
import os

# Directories containing Bandit reports
bandit_report_dirs = [
    "LLM_Responses/bandit_reports/gemini",
    "LLM_Responses/bandit_reports/llama",
    "LLM_Responses/bandit_reports/wizardcoder",
    "LLM_Responses/bandit_reports/mistral",
    "LLM_Responses/bandit_reports/qwen",
    "LLM_Responses/bandit_reports/deepseekcoder",
    "LLM_Responses/bandit_reports/codellama"
]

# Initialize counters
total_files = 0
total_loc = 0
total_high_severity = 0
total_medium_severity = 0
total_low_severity = 0

# Iterate over all Bandit report directories
for bandit_reports_dir in bandit_report_dirs:
    current_loc=0
    current_high_severity=0
    current_medium_severity=0
    current_low_severity=0
    
    for root, _, files in os.walk(bandit_reports_dir):
        for report_file in files:
            if report_file.endswith(".json"):
                total_files += 1
                report_path = os.path.join(root, report_file)

                # Load the Bandit report
                with open(report_path, "r") as f:
                    report = json.load(f)

                # Aggregate metrics
                current_loc += report["metrics"]["_totals"]["loc"]
                current_high_severity += report["metrics"]["_totals"]["SEVERITY.HIGH"]
                current_medium_severity += report["metrics"]["_totals"]["SEVERITY.MEDIUM"]
                current_low_severity += report["metrics"]["_totals"]["SEVERITY.LOW"]

                # Print issues found in the current file
                if report["metrics"]["_totals"]["SEVERITY.HIGH"] > 0:
                    print(f"High severity issues found in {report_path}")
                elif report["metrics"]["_totals"]["SEVERITY.MEDIUM"] > 0:
                    print(f"Medium severity issues found in {report_path}")
                elif report["metrics"]["_totals"]["SEVERITY.LOW"] > 0:
                    print(f"Low severity issues found in {report_path}")
    total_loc += current_loc
    total_high_severity += current_high_severity
    total_medium_severity += current_medium_severity
    total_low_severity += current_low_severity
    print(f"\n{bandit_reports_dir} totals:")
    print(f"Total lines of code (loc): {current_loc}")
    print(f"Total high severity issues: {current_high_severity}")
    print(f"Total medium severity issues: {current_medium_severity}")
    print(f"Total low severity issues: {current_low_severity}")

# Print aggregated results
print("\nAggregated Bandit Report:")
print(f"Total files analyzed: {total_files}")
print(f"Total lines of code (loc): {total_loc}")
print(f"Total high severity issues: {total_high_severity}")
print(f"Total medium severity issues: {total_medium_severity}")
print(f"Total low severity issues: {total_low_severity}")