def is_roaring(n):
    s = str(n)
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        result = ""
        while len(result) < len(s):
            result += str(current)
            current += 1
        if result == s:
            return True
    return False

def next_roaring_year(y):
    y += 1
    while True:
        if is_roaring(y):
            return y
        y += 1

t = int(input())
for i in range(1, t + 1):
    y = int(input())
    z = next_roaring_year(y)
    print(f"Case #{i}: {z}")