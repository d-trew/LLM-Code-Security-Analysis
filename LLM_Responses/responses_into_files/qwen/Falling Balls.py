def build_layout(C, B):
    if sum(B) != C or C < 2:
        return "IMPOSSIBLE"
    
    layout = []
    for i in range(1, C-1):
        if B[i] > 0:
            layout.append("." * (i - 1) + "/" + "\\" * (B[i] - 1) + "." + "\\" * (C - i - 2))
    
    return len(layout), layout

def solve():
    T = int(input())
    results = []
    for t in range(1, T+1):
        C = int(input())
        B = list(map(int, input().split()))
        result = build_layout(C, B)
        if isinstance(result, str):
            results.append(f"Case #{t}: {result}")
        else:
            rows, layout = result
            results.append(f"Case #{t}: {rows}")
            for row in layout:
                results.append(row)
    
    for result in results:
        print(result)

solve()