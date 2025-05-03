def print_logo(printer1, printer2, printer3):
    for c in range(min(printer1)+1):
        for m in range(min(printer2)+1):
            for y in range(min(printer3)+1):
                k = 10**6 - (c + m + y)
                if k >= 0 and c <= printer1[0] and m <= printer2[0] and y <= printer3[0]:
                    return f"{c} {m} {y} {k}"
    return "IMPOSSIBLE"

T = int(input())
for t in range(1, T+1):
    printers = [list(map(int, input().split())) for _ in range(3)]
    print(f'Case #{t}: {print_logo(*printers)}')