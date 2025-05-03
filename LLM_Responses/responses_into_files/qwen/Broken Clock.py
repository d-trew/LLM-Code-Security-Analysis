def find_time(A, B, C):
    for h in range(12):
        for m in range(60):
            for s in range(60):
                n = 0
                while True:
                    ah = (h * 30 + m * 0.5 + s * 1/72) % 360
                    bh = (h * 30 + m * 0.5 + s * 1/72) % 360
                    ch = (h * 30 + m * 0.5 + s * 1/72) % 360
                    if abs(ah - A) < 1e-9 and abs(bh - B) < 1e-9 and abs(ch - C) < 1e-9:
                        return h, m, s, n
                    n += 1

T = int(input())
results = []
for i in range(1, T + 1):
    A, B, C = map(int, input().split())
    h, m, s, n = find_time(A, B, C)
    results.append(f"Case #{i}: {h} {m} {s} {n}")

for result in results:
    print(result)