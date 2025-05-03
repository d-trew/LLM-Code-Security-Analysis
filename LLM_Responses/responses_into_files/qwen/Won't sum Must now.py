def find_min_palindromic_terms(S):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    
    if is_palindrome(S):
        return [S]
    
    for i in range(1, 100):  # Arbitrary limit for K
        for j in range(i + 1, 100):
            k = S - (i * 10**j)
            if k >= 0 and is_palindrome(k):
                return [i] * j + [k]
    
    return [S]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        S = int(data[index])
        result = find_min_palindromic_terms(S)
        results.append(result)
        index += 1
    
    for i, res in enumerate(results, start=1):
        print(f"Case #{i}: {''.join(map(str, res))}")

if __name__ == "__main__":
    main()