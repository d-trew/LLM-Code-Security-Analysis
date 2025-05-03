import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def matrygon_sides(N):
    result = 0
    for i in range(1, N + 1):
        if N % i == 0:
            lcm_val = lcm(i, result)
            gcd_val = gcd(i, result)
            if (N // i) * i > result and gcd_val <= 2 * i:
                result = lcm_val
    return result

def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        print("Case #" + str(t) + ": " + str(matrygon_sides(N)))
        
if __name__ == '__main__':
    main()