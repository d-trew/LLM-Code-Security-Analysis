T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    print(f"Case #{t}:")
    print("+" + "-"*C + "+")
    for r in range(R):
        if r == 0:
            print("|", end="")
            print(".|."*(C-1), end="")
            print("|")
        elif r == R-1:
            print("|", end="")
            print("+-"*C, end="")
            print("+")
        else:
            print("|", end="")
            print(".|."*(C-1), end="")
            print("|")
    print("+" + "-"*C + "+")