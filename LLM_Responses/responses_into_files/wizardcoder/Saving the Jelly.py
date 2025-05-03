import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def closest_sweet(children, sweets):
    min_dist = float('inf')
    closest_child = None
    closest_sweets = []
    for child in children:
        dist = float('inf')
        closest_jelly = None
        for sweet in sweets:
            if sweet != 1:
                d = distance(children[child][0], children[child][1], sweets[sweet][0], sweets[sweet][1])
                if d < dist:
                    dist = d
                    closest_jelly = sweet
        if dist < min_dist or (dist == min_dist and len(closest_sweets) > 0 and child not in [x[0] for x in closest_sweets]):
            min_dist = dist
            closest_sweets = [(child, closest_jelly)]
        elif dist == min_dist:
            closest_sweets.append((child, closest_jelly))
    return closest_sweets

def solve(children, sweets):
    if len(closest_sweet(children, sweets)) > 1:
        return "IMPOSSIBLE"
    
    order = []
    for child in range(2, N+1):
        dist = float('inf')
        closest_jelly = None
        for sweet in range(1, N+1):
            if sweets[sweet] not in [x[1] for x in order]:
                d = distance(children[child][0], children[child][1], sweets[sweet][0], sweets[sweet][1])
                if d < dist:
                    dist = d
                    closest_jelly = sweet
        order.append((child, closest_jelly))
    
    return "POSSIBLE\n" + '\n'.join([f"Case #{i+1}: {x[0]} {x[1]}" for i, x in enumerate(order)] if len(order) == N else "IMPOSSIBLE"

T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    children = {}
    sweets = {}
    for i in range(N):
        x, y = map(int, input().split())
        children[i+1] = (x, y)
        
    for j in range(N+1):
        x, y = map(int, input().split())
        sweets[j+1] = (x, y)
    
    print("Case #{}: {}".format(t), solve(children, sweets))