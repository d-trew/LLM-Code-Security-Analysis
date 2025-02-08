def solve():
    N, K = map(int, input().split())
    U = float(input())
    P = list(map(float, input().split()))

    def calculate_probability(probs):
        dp = {}
        def count_successes(index, successes_so_far, remaining_units):
            if index == N:
                return 1 if successes_so_far >= K else 0
            
            if (index, successes_so_far, remaining_units) in dp:
                return dp[(index, successes_so_far, remaining_units)]

            total_prob = 0
            
            # Option 1: Don't use any units on this core
            total_prob += probs[index] * count_successes(index + 1, successes_so_far + 1, remaining_units) + (1 - probs[index]) * count_successes(index + 1, successes_so_far, remaining_units)
            
            # Option 2: Use some units on this core
            for units_used in range(1, int(remaining_units) + 1):
                new_prob = min(1.0, probs[index] + units_used)
                total_prob += new_prob * count_successes(index + 1, successes_so_far + 1, remaining_units - units_used) + (1 - new_prob) * count_successes(index + 1, successes_so_far, remaining_units - units_used)

            dp[(index, successes_so_far, remaining_units)] = total_prob
            return total_prob

        return count_successes(0, 0, U)

    max_prob = calculate_probability(P)
    return max_prob


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")