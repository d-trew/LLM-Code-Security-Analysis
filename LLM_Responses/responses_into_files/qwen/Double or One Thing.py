def min_lexicographical_string(s):
    n = len(s)
    min_str = 'Z' * (2 * n + 1)
    
    def dfs(index, current, highlight_count):
        nonlocal min_str
        if index == n:
            if len(current) < len(min_str):
                min_str = current
            elif len(current) == len(min_str) and current < min_str:
                min_str = current
            return
        
        # Option 1: Highlight the current character
        dfs(index + 1, current + s[index] * 2, highlight_count + 1)
        
        # Option 2: Do not highlight the current character
        dfs(index + 1, current + s[index], highlight_count)
    
    dfs(0, '', 0)
    return min_str

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(T):
        S = data[i + 1]
        result = min_lexicographical_string(S)
        results.append(f"Case #{i + 1}: {result}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()