import sys
from collections import defaultdict

def main():
    T = int(input())
    for i in range(T):
        AC, AJ = map(int, input().split())
        cam_activities = defaultdict(list)
        jam_activities = defaultdict(list)
        
        for _ in range(AC):
            C, D = map(int, input().split())
            cam_activities[C].append((D, C))
        
        for _ in range(AJ):
            J, K = map(int, input().split())
            jam_activies[J].append((K, J)
            
        min_exchanges = 10**9
        for j in jam_activities.keys():
            for c in cam_activities.keys():
                exchanges = 0
                if j == 0:
                    exchanges += len(cam_activities[c]) + 1
                else:
                    for activity in cam_activities[c]:
                        if (j - 1) % 24 * 60 <= activity[0] < j:
                            exchanges += 1
                min_exchanges = min(min_exchanges, exchanges)
        
        print("Case #%d: %d" % (i+1, min_exchanges))

if __name__ == "__main__":
    main()