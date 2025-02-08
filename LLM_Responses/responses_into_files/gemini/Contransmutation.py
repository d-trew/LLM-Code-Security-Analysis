def solve():
    M = int(input())
    recipes = []
    for _ in range(M):
        recipes.append(list(map(int, input().split())))
    inventory = list(map(int, input().split()))

    adj = [[] for _ in range(M + 1)]
    for i in range(M):
        adj[i + 1].append(recipes[i][0])
        adj[i + 1].append(recipes[i][1])

    def can_produce_unbounded_lead(start_node):
        visited = set()
        q = [start_node]
        visited.add(start_node)
        while q:
            curr = q.pop(0)
            if curr == 1:
                return True
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return False

    if can_produce_unbounded_lead(1):
        return "UNBOUNDED"

    max_lead = inventory[0]
    q = [(inventory, 0)]
    visited = {tuple(inventory)}

    while q:
      curr_inv, curr_lead = q.pop(0)

      for i in range(M):
        if curr_inv[i] > 0:
          next_inv = list(curr_inv)
          next_inv[i] -= 1
          next_inv[recipes[i][0]-1] += 1
          next_inv[recipes[i][1]-1] += 1
          if tuple(next_inv) not in visited:
            visited.add(tuple(next_inv))
            q.append((next_inv, next_inv[0]))
            max_lead = max(max_lead, next_inv[0])

    return max_lead % 1000000007

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")