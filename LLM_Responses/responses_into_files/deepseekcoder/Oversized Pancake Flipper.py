def min_flips(s, k):
    n = len(s)
    s = list(map(int, s))
    flips = 0
    
    for i in range(n - k + 1):
        if s[i] == 1:
            continue
        else:
            flips += 1
            for j in range(k):
                s[i+j] ^= 1
            
    # Check remaining pancakes
    for i in range(n - k + 1, n):
        if s[i] == 0:
            return "IMPOSSIBLE"
    
    return flips

# Read the number of test cases
T = int(input())
for tc in range(1, T+1):
    # Read the string and K
    S, K = input().split()
    K = int(K)
    
    print("Case #{}: {}".format(tc, min_flips(S, K)))