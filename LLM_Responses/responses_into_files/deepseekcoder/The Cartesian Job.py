import sys
from collections import defaultdict

def solve(case_num, lines):
    # Initialize variables
    N = len(lines)
    events = []
    sweep_line = 0

    # Create a dictionary to store the start and end points of each laser's path
    paths = defaultdict(list)
    
    for i in range(N):
        x1, y1, x2, y2 = lines[i]
        
        if (x1 == 0 or x2 == 0) and min(y1, y2) <= 0:
            # The laser starts at the bottom of the line segment
            events.append((0, 1, i))
            events.append((abs(max(y1, y2)), -1, i))
        else:
            # The laser is not starting from the bottom
            if x1 < 0 or (x1 == x2 and y1 < y2):
                continue
            
            k = (y2-y1)/(x2-x1)
            b = y1 - k*x1
            
            intersect_time = (sweep_line-b)/k if k != 0 else float('inf')
            events.append((intersect_time, 1, i))
    
    # Sort the events by time and laser index
    events.sort()
    
    # Iterate through each event
    for e in events:
        _, type, idx = e
        
        if type == 1:
            paths[idx].append(e)
        else:
            intersects = 0
            
            # Check all the lasers that this laser intersects with
            for path_event in paths[idx]:
                if not (path_event[0] < e[0]):
                    break
                
                intersects += 1
            
            # If no intersection is found, return 1.0 as the probability
            if intersects == 0:
                print(f"Case #{case_num}: {1.0}")
                return
    
    # If we reach here, it means that there exists a time interval where all lasers do not intersect with the line segment
    print(f"Case #{case_num}: {0.0}")

T = int(sys.stdin.readline())
for case_num in range(1, T+1):
    N = int(sys.stdin.readline())
    
    lines = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        lines.append((x1, y1, x2, y2))
        
    solve(case_num, lines)