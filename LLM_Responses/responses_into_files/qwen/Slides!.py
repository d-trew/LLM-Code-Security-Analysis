def build_slides(B, M):
    if B == 2:
        if M == 1:
            return "POSSIBLE\n0\n"
        else:
            return "IMPOSSIBLE\n"
    
    if M < (B - 1) or M > ((B * (B - 1)) // 2):
        return "IMPOSSIBLE\n"
    
    result = ["POSSIBLE"]
    for i in range(1, B + 1):
        row = []
        for j in range(1, B + 1):
            if i == j:
                row.append('0')
            elif i < j and (M > (B - 2) or M == ((i * (i - 1)) // 2)):
                row.append('1')
                M -= 1
            else:
                row.append('0')
        result.append(''.join(row))
    
    return '\n'.join(result)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        B = int(data[index])
        M = int(data[index + 1])
        index += 2
        result = build_slides(B, M)
        results.append(result)
    
    for i, res in enumerate(results):
        print(f"Case #{i+1}: {res}")

if __name__ == "__main__":
    main()