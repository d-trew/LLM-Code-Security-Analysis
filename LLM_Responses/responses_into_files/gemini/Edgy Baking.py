import math

def solve():
    N, P = map(int, input().split())
    cookies = []
    for _ in range(N):
        cookies.append(list(map(int, input().split())))

    initial_perimeter = sum(2 * (w + h) for w, h in cookies)
    
    dp = {}
    def solve_recursive(idx, current_perimeter):
        if idx == N:
            return current_perimeter
        
        state = (idx, current_perimeter)
        if state in dp:
            return dp[state]

        # Option 1: Don't cut
        result = solve_recursive(idx + 1, current_perimeter + 2 * (cookies[idx][0] + cookies[idx][1]))

        # Option 2: Cut
        w, h = cookies[idx]
        cut_perimeter = 2 * (w + h + 2 * math.sqrt(w**2 + h**2))
        result = max(result, solve_recursive(idx + 1, current_perimeter + cut_perimeter))

        dp[state] = result
        return result

    max_perimeter = solve_recursive(0,0)
    
    return min(P, max_perimeter)


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")