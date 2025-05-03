import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    activities = [list(map(int, input().split())) for _ in range(N)]
    activities.sort(key=lambda x: (x[0], -x[1]))
    schedule = ['.' * N]
    for start, end in activities:
        if not schedule[-1][start]:
            schedule[-1] = 'C' * (end - start) + schedule[-1]
            continue
        if start <= 0 or end >= 24 * 60:
            schedule[-1] = '.' + schedule[-1]
        else:
            for i in range(len(schedule) - 1, -1, -1):
                if not schedule[i][start]:
                    schedule[i] = 'J' * (end - start) + schedule[i]
                    break
            else:
                schedule[-1] += '.'
                break
    print(f"Case #{{+1}}: {''.join(schedule)}")