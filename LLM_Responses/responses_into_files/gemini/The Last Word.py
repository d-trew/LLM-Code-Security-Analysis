def solve():
    S = input()
    
    import itertools
    
    all_words = []
    
    for perm in itertools.product([0, 1], repeat=len(S) - 1):
        word = S[0]
        for i in range(len(S) - 1):
            if perm[i] == 0:
                word = S[i+1] + word
            else:
                word = word + S[i+1]
        all_words.append(word)
        
    all_words.sort()
    return all_words[-1]

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")