from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = len(input().rstrip())
    moods = list(input().rstrip())
    dp_coding, dp_jamming = 0, 0
    q = deque()
    for i in range(n):
        if i % 2 == 0:
            q.append((i, 'C' if moods[i] == 'J' else 'J'))
        else:
            cur_mood = moods[q[0][0]]
            cur_point = max(10 - dp_coding, 5) if q[0][1] == cur_mood else min(5 + dp_jamming, 10)
            dp_coding, dp_jamming, q.popleft() = dp_coding + cur_point, dp_jamming + cur_point, [(i, 'C' if moods[i] == 'J' else 'J')] if i < n - 1 else (dp_coding, dp_jamming)
    print('Case #{}: {}'.format(_+1, max(dp_coding, dp_jamming)))

This Python code takes as input the number of test cases and the moods of the assistant on each day of the course. It then calculates the maximum score that can be obtained for each test case by using a dynamic programming approach to keep track of the maximum points earned from "Coding" problem sets (dp\_coding) and "Jamming" problem sets (dp\_jamming). The code uses a deque to store the index and mood at each position in the string of moods. For each day, it calculates the maximum number of points that can be earned based on the current day's mood and the most recently requested problem set. Finally, it prints the maximum score for each test case.