def min_operations(S, E):
    if S == E:
        return 0

    def transform(s):
        if s[0] == '1':
            return '0' + s[1:]
        else:
            return '1' + s[1:]

    def double(s):
        return s[:-1]

    queue = [(S, 0)]
    visited = set()
    
    while queue:
        current, steps = queue.pop(0)
        
        if current == E:
            return steps
        
        if current in visited:
            continue
        visited.add(current)
        
        # Apply NOT operation
        not_op = transform(current)
        if not_op not in visited:
            queue.append((not_op, steps + 1))
        
        # Apply double operation
        if len(current) > 1 and current[-1] == '0':
            double_op = double(current)
            if double_op not in visited:
                queue.append((double_op, steps + 1))

    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S, E = data[i].split()
        result = min_operations(S, E)
        results.append(f"Case #{i}: {result}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()