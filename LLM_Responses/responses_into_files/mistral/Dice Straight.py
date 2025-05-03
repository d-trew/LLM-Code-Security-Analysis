import sys
input = sys.stdin.readlines

def longest_straight(dices):
    numbers = sorted(set([sum(sorted([d[j] for d in dices if d[j])) for j in range(6)]))
    return max(1 + len(list(filter(lambda x: x - numbers[i] in numbers, numbers)) for i in range(len(numbers) - 1))

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    dices = [list(map(int, input().strip().split())) for _ in range(N)]
    print(f'Case #{_ + 1}: {longest_straight(dices)}')