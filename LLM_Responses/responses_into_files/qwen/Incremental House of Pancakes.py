def solve_pancakes(L, R):
    n = 0
    while L >= n + 1 or R >= n + 1:
        if L >= R:
            L -= (n + 1)
        else:
            R -= (n + 1)
        n += 1
    return n, L, R

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        L = int(data[index])
        R = int(data[index + 1])
        index += 2
        
        n, l, r = solve_pancakes(L, R)
        results.append(f"Case #{_ + 1}: {n} {l} {r}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()