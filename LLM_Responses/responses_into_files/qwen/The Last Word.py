def find_last_word(S):
    n = len(S)
    for i in range(2**n):
        word = ''
        for j in range(n):
            if (i & (1 << j)):
                word += S[j]
            else:
                word = S[j] + word
        yield word

T = int(input())
for i in range(T):
    S = input()
    words = sorted(list(find_last_word(S)))
    print(f"Case #{i+1}: {words[-1]}")