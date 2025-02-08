import itertools

def solve():
    D = input()
    digits = sorted(D)
    n = len(digits)
    
    min_diff = float('inf')

    for i in range(1 << n):
        group1 = []
        group2 = []
        for j in range(n):
            if (i >> j) & 1:
                group1.append(digits[j])
            else:
                group2.append(digits[j])

        if not group1 or not group2:
            continue

        if '0' == group1[0] or '0' == group2[0]:
            continue

        num1_perms = list(itertools.permutations(group1))
        num2_perms = list(itertools.permutations(group2))

        for p1 in num1_perms:
            for p2 in num2_perms:
                num1 = int("".join(p1))
                num2 = int("".join(p2))
                min_diff = min(min_diff, abs(num1 - num2))

    return min_diff

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")