def solve():
    S, N = input().split()
    N = int(N)
    replacements = [input() for _ in range(N)]

    all_chars = set(list(S))
    for r in replacements:
        all_chars.add(r[0])
        all_chars.add(r[1])

    adj = {c: [] for c in all_chars}
    for r in replacements:
        adj[r[0]].append(r[1])

    visited = set()
    
    def dfs(char):
        visited.add(char)
        for neighbor in adj[char]:
            if neighbor not in visited:
                dfs(neighbor)

    
    num_unique_chars = 0
    for char in all_chars:
        if char not in visited:
            dfs(char)
            num_unique_chars +=1

    
    final_string = list(S)
    for _ in range(len(replacements)):
        for r in replacements:
            new_string = []
            for char in final_string:
                if char == r[0]:
                    new_string.append(r[1])
                else:
                    new_string.append(char)
            final_string = new_string
    
    
    
    return len(set(final_string))



T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")