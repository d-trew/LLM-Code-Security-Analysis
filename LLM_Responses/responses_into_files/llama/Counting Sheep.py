n = int(input())
seen = set()
i = 0
while len(seen) < 10:
    i += 1
    num = str(i * n)
    for digit in num:
        seen.add(digit)
print(f"Case #1: {int(n * (len(seen) + 9))}")