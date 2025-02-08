def solve():
    S = input()
    n = len(S)
    ans = 0
    for i in range(1 << n):
        score = 0
        q = []
        for j in range(n):
            if (i >> j) & 1:  # Request
                if len(q) > 0:
                    continue
                if S[j] == 'C':
                    q.append(('C', 10))
                else:
                    q.append(('J', 5))
            else:  # Submit
                if len(q) == 0:
                    continue
                last_type, max_score = q.pop()
                if S[j] == last_type:
                    score += max_score
                else:
                    score += max_score - 5

        ans = max(ans, score)
    return ans

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")