def solve():
    N = int(input())
    if N == 0:
        return "INSOMNIA"
    
    seen_digits = set()
    i = 1
    while len(seen_digits) < 10:
        current_number = i * N
        for digit in str(current_number):
            seen_digits.add(digit)
        if len(seen_digits) == 10:
            return current_number
        i += 1

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")