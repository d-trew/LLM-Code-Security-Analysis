def solve():
    B, M = map(int, input().split())

    if B == 2:
        if M == 1:
            return "POSSIBLE\n00\n00"
        else:
            return "IMPOSSIBLE"
    
    if B == 3:
        if M == 1:
            return "POSSIBLE\n000\n000\n000"
        elif M == 2:
            return "POSSIBLE\n010\n000\n000"
        elif M == 3:
            return "POSSIBLE\n011\n000\n000"
        else:
            return "IMPOSSIBLE"
    
    if B == 4:
        if M == 1:
            return "POSSIBLE\n0000\n0000\n0000\n0000"
        elif M == 2:
            return "POSSIBLE\n0100\n0000\n0000\n0000"
        elif M == 3:
            return "POSSIBLE\n0110\n0000\n0000\n0000"
        elif M == 4:
            return "POSSIBLE\n0100\n0010\n0000\n0000"
        elif M==5:
            return "POSSIBLE\n0110\n0010\n0000\n0000"
        else:
            return "IMPOSSIBLE"

    
    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")