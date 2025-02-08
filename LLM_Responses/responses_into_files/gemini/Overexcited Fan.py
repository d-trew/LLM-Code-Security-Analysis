def solve():
    X, Y, M = input().split()
    X = int(X)
    Y = int(Y)
    M = M

    px, py = X, Y
    for i in range(len(M)):
        if M[i] == 'N':
            py += 1
        elif M[i] == 'S':
            py -= 1
        elif M[i] == 'E':
            px += 1
        elif M[i] == 'W':
            px -= 1

        if abs(px) + abs(py) <= i + 1:
            return i + 1

    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")