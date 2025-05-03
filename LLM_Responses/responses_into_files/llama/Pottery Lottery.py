T = int(input())
for _ in range(T):
    day = int(input())
    if day == 100:
        V, P = map(int, input().split())
        print(V, P)
    else:
        for _ in range(day-1):
            input()
        V, P = map(int, input().split())
        print(V, P)