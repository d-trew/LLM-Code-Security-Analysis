from fractions import Fraction

def to_int(s):
    return int(s, 16)

def from_int(n, d):
    return format(n % (16**d), f'0{d}X')

def count_hexacoins(N, D, S, E, L):
    s = to_int(S)
    e = to_int(E)
    cnt_total = 0
    cnt_valid = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            a = to_int(L[i])
            b = to_int(L[j])
            if s <= (a + b) % (16**D) <= e:
                cnt_valid += 1
            cnt_total += 1
    
    return Fraction(cnt_valid, cnt_total)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        D = int(data[index + 1])
        S = data[index + 2]
        E = data[index + 3]
        L = data[index + 4:index + 4 + N]
        
        result = count_hexacoins(N, D, S, E, L)
        results.append(f"Case #{_+1}: {result.numerator} {result.denominator}")
        
        index += 4 + N
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()