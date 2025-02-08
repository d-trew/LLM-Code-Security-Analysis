def solve():
    A = int(input())
    prepared = set()
    
    for _ in range(1000):
        i, j = 500, 500
        print(i, j)
        sys.stdout.flush()
        i_prime, j_prime = map(int, input().split())

        if i_prime == 0 and j_prime == 0:
            return
        elif i_prime == -1 and j_prime == -1:
            return
        else:
            prepared.add((i_prime, j_prime))

        
        min_r, max_r = 1001, -1
        min_c, max_c = 1001, -1
        for r, c in prepared:
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
            
        if min_r == 1001:
            continue

        
import sys
T = int(input())
for _ in range(T):
    solve()