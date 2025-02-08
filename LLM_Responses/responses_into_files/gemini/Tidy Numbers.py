def is_tidy(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True

def solve():
    n = int(input())
    
    if is_tidy(n):
        return n
    
    for i in range(n, 0, -1):
        if is_tidy(i):
            return i

t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")