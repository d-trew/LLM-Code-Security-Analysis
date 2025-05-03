def trouble_sort(l):
    n = len(l)
    while True:
        swapped = False
        for i in range(n-2):
            if l[i] > l[i+2]:
                l[i:i+3] = reversed(l[i:i+3])
                swapped = True
        if not swapped:
            break
    return all(l[i] <= l[i+1] for i in range(n-1))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        L = list(map(int, data[index+1:index+N+1]))
        index += N + 1
        
        if trouble_sort(L):
            results.append("OK")
        else:
            for i in range(N-1):
                if L[i] > L[i+1]:
                    results.append(str(i))
                    break
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()