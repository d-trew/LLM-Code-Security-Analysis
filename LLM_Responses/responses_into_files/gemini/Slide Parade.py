def solve():
    B, S = map(int, input().split())
    edges = []
    for _ in range(S):
        u, v = map(int, input().split())
        edges.append((u, v))

    adj = {i: [] for i in range(1, B + 1)}
    for u, v in edges:
        adj[u].append(v)

    def find_path(current_path):
        last_node = current_path[-1]
        if last_node == 1 and len(current_path) > 1:
            counts = {}
            for node in current_path:
                counts[node] = counts.get(node, 0) + 1
            
            valid = True
            first_count = counts[1]
            for node in counts:
                if node != 1 and counts[node] != first_count -1:
                    valid = False
                    break
            if valid:
                return current_path

        for neighbor in adj[last_node]:
            new_path = find_path(current_path + [neighbor])
            if new_path:
                return new_path
        return None

    path = find_path([1])

    if path:
        return len(path), path
    else:
        return None, None

T = int(input())
for i in range(1, T + 1):
    length, path = solve()
    if path:
        print(f"Case #{i}: {length}")
        print(*path)
    else:
        print(f"Case #{i}: IMPOSSIBLE")