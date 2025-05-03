def min_flips(s):
    flips = 0
    i = 0
    while i < len(s):
        if s[i] == '-':
            flips += 1
            if i + 1 < len(s) and s[i+1] == '+':
                i += 2
            else:
                i += 1
        else:
            i += 1
    return flips

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    for t in range(1, T+1):
        s = data[t]
        result = min_flips(s)
        results.append(f"Case #{t}: {result}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()