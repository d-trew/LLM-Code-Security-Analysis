from itertools import permutations
import sys
input = sys.stdin.readline

def min_diff(digits):
    digits = list(set(digits))  # Remove duplicates
    if len(digits) < 2 or not any(d != '0' for d in digits):
        return -1
    diff_min = float('inf')

    for i in range(2, len(digits)+1):
        for pair in permutations(digits, i):
            if all(pair[0] < pair[1] for pair in zip(pair, sorted(pair, reverse=True))):  # Ensure no leading zeros
                num1 = int(''.join(str(d) for d in pair[:i]))
                num2 = int(''.join(str(d) for d in digits[i:]))
                diff = abs(num1 - num2)
                diff_min = min(diff, diff_min)

    return diff_min if diff_min != float('inf') else -1

T = int(input())
for _ in range(T):
    print(f"Case #{_+1}: {min_diff(input().strip())}")