def solve():
    R, C = map(int, input().split())

    if (R * C) < 5 or (R > 5 and C > 5):
      return "IMPOSSIBLE"

    if R == 2 and C == 2:
        return "IMPOSSIBLE"
    if R == 2 and C == 3:
        return "IMPOSSIBLE"
    if R == 3 and C == 2:
        return "IMPOSSIBLE"

    if R == 2 and C == 4:
        return "IMPOSSIBLE"
    if R == 4 and C == 2:
        return "IMPOSSIBLE"

    if R == 3 and C == 3:
      return "IMPOSSIBLE"


    if R == 5 and C == 5:
      return "IMPOSSIBLE"


    
    
    
    
    return "POSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")