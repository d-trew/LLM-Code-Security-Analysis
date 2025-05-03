def check_magnificent(arr):
    N = len(arr)
    failed_pairs = []
    
    for i in range(N):
        x1, y1, x2, y2 = arr[i]
        for j in range(i + 1, N):
            x3, y3, x4, y4 = arr[j]
            det = (x1 - x2) * (y3 - y4) - (x3 - x4) * (y1 - y2)
            if det == 0:
                continue
            t = ((x1 - x3) * (y3 - y4) - (x3 - x4) * (y1 - y3)) / det
            u = -((x1 - x2) * (y1 - y3) - (x3 - x4) * (y1 - y2)) / det
            if 0 <= t <= 1 and 0 <= u <= 1:
                continue
            failed_pairs.append(i + 1)
            break
    
    if not failed_pairs:
        return "MAGNIFICENT"
    else:
        return " ".join(map(str, sorted(set(failed_pairs))))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        arr = []
        for _ in range(N):
            x1, y1, x2, y2 = map(int, data[index:index+4])
            arr.append((x1, y1, x2, y2))
            index += 4
        
        results.append(check_magnificent(arr))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()