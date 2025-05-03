n = int(input())
for i in range(1, n+1):
    s = str(i)
    if s == "".join(sorted(s)):
        print(f"Case #{i}: {s}")