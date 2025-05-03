def prime_time():
    T = int(input())
    for i in range(T):
        M = int(input())
        primes = []
        counts = []
        for _ in range(M):
            P, N = map(int, input().split())
            primes.append(P)
            counts.append(N)
        # check if there is a valid split of cards
        def is_valid_split():
            sum_counts = sum(counts)
            for i in range(M):
                for j in range(i+1, M):
                    left_sum = primes[i] * counts[i]
                    right_product = 1
                    for k in range(j, M):
                        right_product *= primes[k] ** counts[k]
                    if left_sum == right_product:
                        return True
            return False
        
        # find the maximum score of a valid split
        def max_score():
            max_score = 0
            for i in range(M):
                for j in range(i+1, M):
                    left_sum = primes[i] * counts[i]
                    right_product = 1
                    for k in range(j, M):
                        right_product *= primes[k] ** counts[k]
                    if left_sum == right_product:
                        max_score = max(max_score, left_sum)
            return max_score
        
        # main logic
        if is_valid_split():
            print("Case #{}: {}".format(i+1, max_score()))
        else:
            print("Case #{}: 0".format(i+1))
            
prime_time()