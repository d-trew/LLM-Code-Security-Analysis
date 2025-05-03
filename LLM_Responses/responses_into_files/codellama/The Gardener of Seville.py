import sys

# Number of test cases
T = int(sys.stdin.readline())

for t in range(1, T+1):
    # Number of rows and columns of the courtyard
    R, C = map(int, sys.stdin.readline().split())
    
    # List of all possible hedge maze configurations
    hedges = []
    
    for r in range(R):
        for c in range(C):
            if r == 0 and c == 0:
                continue
            elif r == R-1 and c == C-1:
                continue
            else:
                hedges.append((r, c))
    
    # List of all possible paths for each courtier to follow
    paths = []
    
    for i in range(2*R*C):
        paths.append([])
    
    for r in range(R):
        for c in range(C):
            if r == 0 and c == 0:
                continue
            elif r == R-1 and c == C-1:
                continue
            else:
                paths[i].append((r, c))
    
    # List of all possible pairs of courtiers in love
    loves = []
    
    for line in sys.stdin.readlines():
        loves.append(list(map(int, line.split())))
    
    # Check if it is possible to construct a hedge maze that satisfies all conditions
    for i in range(len(lovest)):
        for j in range(i+1, len(lovest)):
            if loves[i][0] == loves[j][0] or loves[i][1] == loves[j][1]:
                continue
            else:
                found = False
                for k in range(len(hedges)):
                    if (lovest[i][0], lovest[j][0]) in hedges[k]:
                        paths[lovest[i][0]].append((lovest[j][1], lovest[i][1]))
                        paths[lovest[j][0]].append((lovest[i][1], lovest[j][1]))
                        found = True
                        break
                if not found:
                    print("IMPOSSIBLE")
                    sys.exit()
    
    # Output the hedge maze that satisfies all conditions
    print("Case #{}:".format(t))
    for r in range(R):
        for c in range(C):
            if (r, c) in hedges:
                print("/", end="")
            else:
                print(" ", end="")
        print()