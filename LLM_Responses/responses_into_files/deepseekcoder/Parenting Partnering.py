def min_exchanges():
    T = int(input())
    for t in range(T):
        AC, AJ = map(int, input().split())
        activities = []
        for _ in range(AC + AJ):
            start, end = map(int, input().split())
            activities.append((start, end))
        activities.sort()
        
        exchanges = 0
        current_end = 0
        for start, end in activities:
            if start < current_end:  # overlapping activity
                current_end = min(current_end, end)  # merge overlapping activities
            else:  # no overlap
                current_end = end
        exchanges += 1 if current_end < 720 else 0  # check last activity
        
        print("Case #{}: {}".format(t + 1, exchanges))
min_exchanges()