def solve():
    printers = []
    for _ in range(3):
        printers.append(list(map(int, input().split())))

    min_c = min(p[0] for p in printers)
    min_m = min(p[1] for p in printers)
    min_y = min(p[2] for p in printers)
    min_k = min(p[3] for p in printers)

    total = min_c + min_m + min_y + min_k

    if total > 10**6:
        c = min_c
        m = min_m
        y = min_y
        k = 10**6 - c - m - y
        if k < 0:
            return "IMPOSSIBLE"
        
        
        
    elif total < 10**6:
        
        remaining = 10**6 - total
        
        if min_k + remaining <= 10**6 :
            k = min_k + remaining
            c = min_c
            m = min_m
            y = min_y

        elif min_y + remaining <= 10**6:
            y = min_y + remaining
            c = min_c
            m = min_m
            k = min_k
        elif min_m + remaining <= 10**6:
            m = min_m + remaining
            c = min_c
            y = min_y
            k = min_k
        elif min_c + remaining <= 10**6:
            c = min_c + remaining
            m = min_m
            y = min_y
            k = min_k
        else:
            return "IMPOSSIBLE"

            
            
    else:
        c = min_c
        m = min_m
        y = min_y
        k = min_k


    if all(c <= p[0] and m <= p[1] and y <= p[2] and k <= p[3] for p in printers):
        return f"{c} {m} {y} {k}"
    else:
        return "IMPOSSIBLE"

t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")