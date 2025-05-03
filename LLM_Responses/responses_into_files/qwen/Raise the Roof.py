def find_roof_ordering(columns):
    n = len(columns)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if (columns[l][2] > columns[i][2] and
                            columns[l][2] > columns[j][2] and
                            columns[l][2] > columns[k][2]):
                        return [i+1, j+1, k+1, l+1]
    return []

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        columns = []
        index += 1
        for _ in range(n):
            x, y, h = map(int, data[index:index+3])
            columns.append((x, y, h))
            index += 3
        
        result = find_roof_ordering(columns)
        results.append(f"Case #{_ + 1}: {' '.join(map(str, result))}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()