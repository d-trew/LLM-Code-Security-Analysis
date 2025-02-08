import json
import os

# Directories containing Bandit reports
bandit_report_dirs = [
    "LLM_Responses/bandit_reports/gemini",
    "LLM_Responses/bandit_reports/LLAMA"
]

# Initialize counters
total_files = 0
total_loc = 0
total_high_severity = 0
total_medium_severity = 0
total_low_severity = 0

# Iterate over all Bandit report directories
for bandit_reports_dir in bandit_report_dirs:
    for root, _, files in os.walk(bandit_reports_dir):
        for report_file in files:
            if report_file.endswith(".json"):
                total_files += 1
                report_path = os.path.join(root, report_file)

                # Load the Bandit report
                with open(report_path, "r") as f:
                    report = json.load(f)

                # Aggregate metrics
                total_loc += report["metrics"]["_totals"]["loc"]
                total_high_severity += report["metrics"]["_totals"]["SEVERITY.HIGH"]
                total_medium_severity += report["metrics"]["_totals"]["SEVERITY.MEDIUM"]
                total_low_severity += report["metrics"]["_totals"]["SEVERITY.LOW"]

                # Print issues found in the current file
                if report["metrics"]["_totals"]["SEVERITY.HIGH"] > 0:
                    print(f"High severity issues found in {report_path}")
                elif report["metrics"]["_totals"]["SEVERITY.MEDIUM"] > 0:
                    print(f"Medium severity issues found in {report_path}")
                elif report["metrics"]["_totals"]["SEVERITY.LOW"] > 0:
                    print(f"Low severity issues found in {report_path}")

# Print aggregated results
print("\nAggregated Bandit Report:")
print(f"Total files analyzed: {total_files}")
print(f"Total lines of code (loc): {total_loc}")
print(f"Total high severity issues: {total_high_severity}")
print(f"Total medium severity issues: {total_medium_severity}")
print(f"Total low severity issues: {total_low_severity}")