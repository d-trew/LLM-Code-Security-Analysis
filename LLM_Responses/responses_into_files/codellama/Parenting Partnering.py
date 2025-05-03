from math import inf

def min_exchanges(Cameron, Jamie):
    end_time = 24 * 60
    Cameron_activities = sorted([(Ci, Di) for Ci, Di in zip(*[iter(Cameron[i:i+2]) for i in range(0, len(Cameron), 2)]))
    Jamie_activities = sorted([(Ji, Ki) for Ji, Ki in zip(*[iter(Jamie[i:i+2]) for i in range(0, len(Jamie), 2)]])
    
    free_time = [end_time]
    for Ci, Di in Cameron_activities:
        free_time.append(Ci)
        free_time.append(Di)
    for Ji, Ki in Jamie_activities:
        free_time.append(Ji)
        free_time.append(Ki)

    exchanges = 0
    prev_free_time = 0
    for time in sorted(free_time):
        if time > prev_free_time:
            exchanges += 1
        prev_free_time = time

    return exchanges

T = int(input())
for i in range(1, T + 1):
    AC, AJ = map(int, input().split())
    Cameron = [int(x) for x in input().split()] * (AC // 2)
    Jamie = [int(x) for x in input().split()] * (AJ // 2)
    
    print(f"Case #{i}: {min_exchanges(Cameron, Jamie)}")