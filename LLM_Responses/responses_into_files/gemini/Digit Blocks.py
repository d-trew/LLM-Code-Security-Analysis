T, N, B, P = map(int, input().split())
total_score = 0
for t in range(T):
    towers = [[] for _ in range(N)]
    for b in range(N * B):
        D = int(input())
        shortest_tower = 0
        for i in range(1, N):
            if len(towers[i]) < len(towers[shortest_tower]):
                shortest_tower = i
        print(shortest_tower + 1)
        towers[shortest_tower].append(D)
    score = 0
    for tower in towers:
        num = 0
        for digit in tower:
            num = num * 10 + digit
        score += num
    total_score += score
    if t < T - 1:
        continue
    result = int(input())
    if result == -1:
        break