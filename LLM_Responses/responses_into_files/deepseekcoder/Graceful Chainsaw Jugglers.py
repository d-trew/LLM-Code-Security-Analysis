def max_jugglers(R, B):
    # Initialize maximum number of jugglers as min of R and B
    max_jugglers = min(R, B)
    
    # If both chainsaws are equal in number, return half of the total
    if R == B:
        max_jugglers //= 2
        
    return max_jugglers

T = int(input().strip())
for tc in range(1, T+1):
    R, B = map(int, input().split())
    print("Case #{}: {}".format(tc, max_jugglers(R, B)))