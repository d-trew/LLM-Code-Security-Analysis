import sys

def solve(n_test):
    n_holes = int(input())
    holes = []
    for i in range(n_holes):
        x, y = map(int, input().split())
        holes.append((x,y))
    
    wormholes = {}
    for hole1, hole2 in combinations(holes, 2):
        if (hole1[0] == hole2[0] or hole1[1] == hole2[1]) and (hole1 != hole2):
            wormholes[(hole1, hole2)] = True
    
    n_touched = 0
    for i in range(n_test):
        x, y = map(int, input().split())
        if (x,y) in holes:
            n_touched += 1
            
        elif (x,y) in wormholes:
            n_touched += 2
    
    return n_touched

def main():
    t = int(input())
    for i in range(t):
        print("Case #" + str(i+1) + ": " + str(solve(i+1)))
        
if __name__ == "__main__":
    main()