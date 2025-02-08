import re

def count_matches(A, B, R):
    count = 0
    for i in range(A, B + 1):
        if re.match(R, str(i)):
            count += 1
    return count

T = int(input())
for x in range(1, T + 1):
    A, B = map(int, input().split())
    R = input()
    y = count_matches(A, B, R)
    print(f'Case #{x}: {y}')