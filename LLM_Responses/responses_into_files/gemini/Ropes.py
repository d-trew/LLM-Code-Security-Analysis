T, N, W = map(int, input().split())

wins = 0
for _ in range(T):
    north = list(range(1, 2 * N + 1))
    south = list(range(1, 2 * N + 1))
    north_used = [False] * (2 * N)
    south_used = [False] * (2 * N)
    my_score = 0
    opponent_score = 0

    for i in range(N):
        # My turn
        a = north.index(min(north)) + 1
        b = south.index(min(south)) + 1
        print(a, b)
        
        north_used[a-1] = True
        south_used[b-1] = True
        
        
        
        # Opponent's turn
        c, d = map(int, input().split())
        
        north_used[c-1] = True
        south_used[d-1] = True

    result = int(input())
    wins += result

print(wins)