import re

def match_patterns(patterns):
    if len(patterns) == 1:
        return patterns[0]
    
    for i in range(len(patterns)):
        pattern = patterns[i]
        if '*' not in pattern:
            continue
        
        for j, other_pattern in enumerate(patterns):
            if i == j:
                continue
            if '*' not in other_pattern:
                continue
            
            # Check if we can replace the asterisk in the current pattern to match the other pattern
            for k in range(len(other_pattern)):
                if other_pattern[k] != '*':
                    new_pattern = pattern[:k] + other_pattern[k] + pattern[k+1:]
                    if re.fullmatch(new_pattern, other_pattern):
                        break
            else:
                continue
            break
        else:
            return '*'
    
    # If we reach here, it means all patterns can be matched by the same name
    return 'A' * 104

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        patterns = data[index + 1:index + 1 + N]
        index += 1 + N
        
        result = match_patterns(patterns)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()