n = int(input())
for _ in range(n):
    N = int(input())
    design = []
    for _ in range(N):
        link1, link2 = map(int, input().split())
        design.append((link1 - 1, link2 - 1))
    print(N)
    for link in design:
        print(*link)