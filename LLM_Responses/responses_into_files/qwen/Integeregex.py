import re

def count_matches(regex, A, B):
    count = 0
    for i in range(A, B + 1):
        if re.match(regex, str(i)):
            count += 1
    return count

T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    regex = input()
    result = count_matches(regex, A, B)
    print(f"Case #{t}: {result}")