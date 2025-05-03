import sys

def get_picture(x, y, m):
    if len(m) == 0:
        return "IMPOSSIBLE"
    
    north = 0
    east = 0
    south = 0
    west = 0
    
    for i in range(len(m)):
        if m[i] == "N":
            north += 1
        elif m[i] == "E":
            east += 1
        elif m[i] == "S":
            south += 1
        elif m[i] == "W":
            west += 1
    
    if x + east > 0 and y + north > 0:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

T = int(input())
for i in range(T):
    x, y, m = input().split()
    print("Case #" + str(i+1) + ": " + get_picture(x, y, m))