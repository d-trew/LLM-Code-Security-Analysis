import re

def solve(s):
    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    phone_number = sorted([digits.index(c) for c in s if c in ''.join(digits)] + [9]*((3 - len(s)) if len(s) < 10 else 0))
    return ' '.join(str(i+1) for i in phone_number)

T = int(input())
for _ in range(T):
    print(f"Case #{_+1}: {solve(input())}")