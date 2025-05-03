# Test cases
T = int(input())
for t in range(T):
    # Read input
    S, N = input().split()
    R = []
    for i in range(N):
        R.append(input().split())
    
    # Perform replacements
    text = S
    for r in R:
        a, b = r[0], r[1]
        text = text.replace(a, b)
    
    # Count unique characters
    unique_chars = set()
    for c in text:
        if c not in unique_chars:
            unique_chars.add(c)
    
    print("Case #{}: {}".format(t+1, len(unique_chars)))