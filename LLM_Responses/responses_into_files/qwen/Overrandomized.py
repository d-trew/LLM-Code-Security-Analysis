from collections import defaultdict

def decode_digit_string(U, queries):
    D = [''] * 10
    for Qi, Ri in queries:
        if Qi != -1:
            for j in range(len(Ri)):
                if D[j] == '':
                    D[j] = chr(ord('A') + (Qi % 26))
                Qi //= 26
    
    return ''.join(D)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        U = int(data[index])
        index += 1
        
        queries = []
        for _ in range(10**U):
            Qi = int(data[index])
            Ri = data[index + 1]
            index += 2
            queries.append((Qi, Ri))
        
        D = decode_digit_string(U, queries)
        results.append(D)
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()