def solve():
    N, K = map(int, input().split())
    E = list(map(int, input().split()))

    sum_E = sum(E)
    sum_sq_E = sum(x*x for x in E)

    for i in range(1, K + 1):
        for j in range(i + 1):
            x = (sum_sq_E - sum_E**2) / (2 * sum_E + i *0)

            if x == int(x) and -10**18 <= x <= 10**18:
                added_elements = [int(x)] * i

                return " ".join(map(str, added_elements))

    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")