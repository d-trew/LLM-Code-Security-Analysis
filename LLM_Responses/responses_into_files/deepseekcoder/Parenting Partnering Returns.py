def solve(activities):
    # Sort the activities by their end time.
    activities.sort(key=lambda x: x[1])
    
    # Initialize two lists to store Cameron's and Jamie's activities.
    cameron = []
    jamie = []
    
    for activity in activities:
        if not cameron or cameron[-1][1] < activity[0]:
            cameron.append(activity)
        elif not jamie or jamie[-1][1] < activity[0]:
            jamie.append(activity)
        else:
            return "IMPOSSIBLE"
    
    return "".join(['C' if i % 2 == 0 else 'J' for i in range(len(cameron + jamie))])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    activities = [tuple(map(int, input().split())) for _ in range(N)]
    result = solve(activities)
    print("Case #{}: {}".format(t, result))