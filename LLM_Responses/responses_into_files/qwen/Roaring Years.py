def find_next_roaring_year(y):
    while True:
        y += 1
        str_y = str(y)
        length = len(str_y)
        for i in range(1, length):
            if int(str_y[:i]) + 1 == int(str_y[i:i+1]):
                continue
            else:
                break
        else:
            return y

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        Y = int(data[i])
        next_roaring_year = find_next_roaring_year(Y)
        results.append(f"Case #{i}: {next_roaring_year}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()