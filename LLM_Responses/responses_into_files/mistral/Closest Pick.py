import fractions
from collections import defaultdict
input = __import__('sys').stdin.read().splitlines()
T = int(input[0])
for t in range(1, T+1):
    N, K = map(int, input[1].split())
    tickets = list(map(int, input[2].split()))
    dist_dict = defaultdict(lambda: float('inf'))
    for ticket in tickets:
        dist_dict[ticket] = 0
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            dist = max(abs(i-j), abs(K-i-j))
            for ticket in tickets:
                dist_dict[ticket] = min(dist_dict[ticket], dist)
    win_prob = sum([min(1, 2/(dist_dict[i]+1)) for i in range(1, K+1)])
    print(f"Case #{t}: {win_prob}")