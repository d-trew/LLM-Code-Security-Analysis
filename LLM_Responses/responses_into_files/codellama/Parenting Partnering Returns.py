import sys

def main():
    t = int(input())
    
    for i in range(1, t + 1):
        n = int(input())
        
        activities = []
        for j in range(n):
            start, end = map(int, input().split())
            activities.append((start, end))
            
        print("Case #" + str(i) + ":", end="")
        
        if not valid_schedule(activities):
            print("IMPOSSIBLE")
        else:
            for activity in activities:
                if activity[0] % 2 == 0:
                    print("C", end="")
                else:
                    print("J", end="")
            
def valid_schedule(activities):
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            if (activities[i][0] < activities[j][0] and activities[i][1] > activities[j][0]) or (activities[i][0] > activities[j][0] and activities[i][1] < activities[j][0]):
                return False
    return True

if __name__ == "__main__":
    main()