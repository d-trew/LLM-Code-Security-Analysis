def solve():
    R, S = map(int, input().split())
    
    ans = []
    a = R
    b = 1
    for i in range(S - 1):
        ans.append((a, b))
        a -= 1
        b += R

    return len(ans), ans

T = int(input())
for i in range(1, T + 1):
    num_ops, ops = solve()
    print(f"Case #{i}: {num_ops}")
    for a, b in ops:
        print(a, b)