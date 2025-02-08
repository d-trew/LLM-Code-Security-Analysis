def solve():
    N = int(input())
    F = list(map(int, input().split()))
    F = [x - 1 for x in F]  # Adjust to 0-based indexing

    max_circle_size = 0

    # Iterate through all possible starting nodes
    for start_node in range(N):
        current_circle = [start_node]
        current_node = start_node
        next_node = F[current_node]

        while next_node != start_node and next_node not in current_circle:
            current_circle.append(next_node)
            current_node = next_node
            next_node = F[current_node]

        # Check if a circle is formed
        if next_node == start_node and len(current_circle) > 1:
            max_circle_size = max(max_circle_size, len(current_circle))

    #Consider pairs
    max_pair_size = 0
    for i in range(N):
        for j in range(i+1,N):
            if F[i] == j and F[j] == i:
                max_pair_size = max(max_pair_size,2)

    return max(max_circle_size,max_pair_size)


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")