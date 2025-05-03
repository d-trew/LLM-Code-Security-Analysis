import sys

def find_schedule(activities):
    activities.sort()
    cam_activities = []
    jamie_activities = []

    for start, end in activities:
        if not cam_activities or cam_activities[-1][1] < start:
            cam_activities.append((start, end))
        else:
            jamie_activities.append((start, end))

    return 'C' * len(cam_activities) + 'J' * len(jamie_activities)

T = int(sys.stdin.readline().strip())
for t in range(1, T+1):
    N = int(sys.stdin.readline().strip())
    activities = []
    for i in range(N):
        start, end = map(int, sys.stdin.readline().split())
        activities.append((start, end))
    print(f"Case #{t}: {find_schedule(activities) if all(not overlap(cam_activities, jamie_activities)) else 'IMPOSSIBLE'}")