import sys

# Read input from stdin
T = int(input())

for i in range(T):
    # Read number of computers and links
    N, L = map(int, input().split())
    
    # Create a list of all possible permutations of the numbers 1 to N
    permutations = []
    for i in range(N):
        permutations.append([])
        for j in range(i+1, N):
            permutations[i].append((j, j+1))
    
    # Choose a random permutation from the list of all possible permutations
    f = random.choice(permutations)
    
    # Create a copy of the network design with the chosen permutation
    g = []
    for i in range(N):
        g.append([])
        for j in range(i+1, N):
            if f[i][j-1] == 0:
                continue
            g[i].append((f[i][j-1], f[j][i-1]))
    
    # Print the copy of the network design
    print(N)
    for i in range(N):
        for j in range(i+1, N):
            if g[i][j-1] == 0:
                continue
            print(g[i][j-1], g[j][i-1])
    
    # Read the list of Xs from stdin
    X = []
    for i in range(N):
        X.append(int(input()))
    
    # Check if the list of Xs is equal to the original permutation
    if X == f:
        print("OK")
    else:
        print("Wrong Answer")