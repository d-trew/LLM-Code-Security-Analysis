import math

def solve(A, B, C):
    hours = int((C + 360) // 720) % 12
    minutes = int(((B + 360) // 12 - hours * 60) % 60)
    seconds = int((A + 360 - (hours * 360 + minutes * 12)) / 60)
    nanoseconds = (A + math.floor(B / 12) + math.floor(C / 720) * 60 * 12) % (10 ** 9)
    return f'Case #{test_case}: {hours} {minutes} {seconds} {nanoseconds}'

T = int(input())
for _ in range(T):
    test_case, A, B, C = map(int, input().split())
    print(solve(A, B, C))