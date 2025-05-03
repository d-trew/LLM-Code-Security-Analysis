T = int(input())
for _ in range(T):
    R, S = map(int, input().split())
    operations = 0
    for r in range(R):
        for s in range(1, S+1):
            print(f"{r*S+1} {s}")
        operations += (S - 1)
    print(f"Case #{_+1}: {operations}")