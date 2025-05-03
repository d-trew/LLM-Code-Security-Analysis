from itertools import combinations

def max_score(primes, counts):
    total_sum = sum(p * c for p, c in zip(primes, counts))
    primes_counts = list(zip(primes, counts))

    def product(lst):
        return 1 if not lst else lst[0] * product(lst[1:])

    def find_group(total, target_product, start=0):
        for r in range(1, len(primes_counts) - start + 1):
            for combo in combinations(primes_counts[start:], r):
                if sum(p * c for p, c in combo) == total and product([p for p, _ in combo]) == target_product:
                    return True
        return False

    max_score = 0
    for i in range(1, len(primes_counts)):
        for j in range(1, len(primes_counts) - i):
            first_group_sum = sum(p * c for p, c in primes_counts[:i])
            second_group_product = product([p for p, _ in primes_counts[i:i+j]])
            if first_group_sum == second_group_product:
                max_score = max(max_score, first_group_sum)
            if find_group(total_sum - first_group_sum, second_group_product):
                return total_sum

    return max_score

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    for _ in range(T):
        M = int(data[index])
        index += 1
        primes = []
        counts = []
        for _ in range(M):
            P = int(data[index])
            N = int(data[index + 1])
            primes.append(P)
            counts.append(N)
            index += 2
        
        result = max_score(primes, counts)
        results.append(result)
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    solve()