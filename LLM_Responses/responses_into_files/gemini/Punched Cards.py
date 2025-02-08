def solve():
    R, C = map(int, input().split())
    
    print("..+" + "+-+" * (C - 1))
    for i in range(R):
        print("..|" + "|." * (C - 1) + "|")
        print("+-+" * C)
        if i < R -1:
            print("..|" + "|." * (C - 1) + "|")

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}:")
    solve()