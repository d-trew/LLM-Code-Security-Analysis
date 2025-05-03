import random

def solve():
    T, N, B, P = map(int, input().split())
    towers = [[0]*B for _ in range(N)]
    score = 0

    for _ in range(T):
        digit = int(input())

        # Find the first empty tower or the one with less than B blocks
        for i in range(1, N+1):
            if sum(towers[i-1]) < B:
                towers[i-1].append(digit)
                score += 10**(len(towers[i-1]) - 1) * digit
                break

    print(score)

solve()