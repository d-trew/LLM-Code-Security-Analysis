import json
from collections import defaultdict

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
    
    # Print detailed report
    print("CWE-Tagged Issues by LLM:\n")
    for llm in sorted(llm_cwe_counts.keys()):
        print(f"{llm.upper()}:")
        total = sum(llm_cwe_counts[llm].values())
        print(f"  Total CWE-tagged issues: {total}")
        
        for cwe, count in sorted(llm_cwe_counts[llm].items()):
            # Find first matching rule for description
            desc = next((v['description'] for k,v in cwe_descriptions.items() 
                        if v['cwe'] == cwe), "No description available")
            print(f"  {cwe}: {count} occurrences")
            print(f"    Description: {desc[:120]}...")
            print(f"    Example rules: {', '.join(k for k,v in cwe_descriptions.items() if v['cwe'] == cwe)[:60]}...")
            print()

if __name__ == "__main__":
    sarif_path = "LLM_Responses/codeql_reports/all_results.sarif"
    analyze_cwe_issues(sarif_path)