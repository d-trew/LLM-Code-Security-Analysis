def pancake_flipping(S):
    n = len(S)
    flips = 0
    for i in range(n, 0, -1):
        if S[i-1] == '-':
            k = i
            while S[k-1] == '-':
                k -= 1
            S = '-' * (i-k) + '+' * k + S[k+1:]
            flips += 1
    return flips

for i in range(int(input())):
    S = input()
    print(f"Case #{i+1}: {pancake_flipping(S)}")