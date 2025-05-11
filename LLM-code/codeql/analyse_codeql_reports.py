import json
from collections import defaultdict
import os

def analyze_cwe_issues(sarif_path):
    with open(sarif_path) as f:
        data = json.load(f)
    
    # Initialize data structures
    llm_cwe_counts = defaultdict(lambda: defaultdict(int))
    cwe_descriptions = {}
    rule_severities = {}
    
    # Process rules metadata first
    for rule in data.get('runs', [{}])[0].get('tool', {}).get('driver', {}).get('rules', []):
        rule_id = rule['id']
        if 'properties' in rule and 'tags' in rule['properties']:
            for tag in rule['properties']['tags']:
                if tag.startswith('external/cwe/cwe-'):
                    cwe = tag.split('/')[-1].upper()
                    cwe_descriptions[rule_id] = {
                        'cwe': cwe,
                        'description': rule['fullDescription']['text'],
                        'severity': rule['properties'].get('problem.severity', 'warning')
                    }
    
    # Process results
    for result in data.get('runs', [{}])[0].get('results', []):
        if not result.get('locations'):
            continue
            
        # Extract LLM name
        file_path = result['locations'][0]['physicalLocation']['artifactLocation']['uri']
        llm = file_path.split('/')[0]
        rule_id = result.get('ruleId')
        
        # Count CWEs
        if rule_id in cwe_descriptions:
            cwe = cwe_descriptions[rule_id]['cwe']
            llm_cwe_counts[llm][cwe] += 1
    

    output_dir = "LLM_Responses/codeql_reports"
    output_file = os.path.join(output_dir, "codeql_cwe_analysis_results.txt")
    
    # Write results to file
    with open(output_file, 'w') as f:
        # Write detailed report
        f.write("CWE-Tagged Issues by LLM:\n\n")
        for llm in sorted(llm_cwe_counts.keys()):
            f.write(f"{llm.upper()}:\n")
            total = sum(llm_cwe_counts[llm].values())
            f.write(f"  Total CWE-tagged issues: {total}\n")
            
            for cwe, count in sorted(llm_cwe_counts[llm].items()):
                # Find first matching rule for description
                desc = next((v['description'] for k,v in cwe_descriptions.items() 
                            if v['cwe'] == cwe), "No description available")
                f.write(f"  {cwe}: {count} occurrences\n")
                f.write(f"    Description: {desc[:120]}...\n")
                f.write(f"    Example rules: {', '.join(k for k,v in cwe_descriptions.items() if v['cwe'] == cwe)[:60]}...\n")
                f.write("\n")

        # Write summary statistics
        f.write("\n=== SUMMARY STATISTICS ===\n")
        total_issues = sum(sum(counts.values()) for counts in llm_cwe_counts.values())
        unique_cwes = set()
        for counts in llm_cwe_counts.values():
            unique_cwes.update(counts.keys())
        
        f.write(f"Total CWE-tagged issues across all LLMs: {total_issues}\n")
        f.write(f"Unique CWEs identified: {len(unique_cwes)}\n")
        f.write("List of unique CWEs: " + ", ".join(sorted(unique_cwes)) + "\n")

    # Also print to console
    print(f"\nAnalysis complete. Results saved to {output_file}")

if __name__ == "__main__":
    sarif_path = "LLM_Responses/codeql_reports/all_results.sarif"
    analyze_cwe_issues(sarif_path)