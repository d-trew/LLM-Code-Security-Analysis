def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        sold = [False] * N
        for i in range(N):
            line = list(map(int, input().split()))
            D = line[0]
            preferences = line[1:]
            
            best_choice = -1
            for pref in preferences:
                if not sold[pref]:
                    best_choice = pref
                    break
            print(best_choice)
            
            if best_choice != -1:
                sold[best_choice] = True

solve()