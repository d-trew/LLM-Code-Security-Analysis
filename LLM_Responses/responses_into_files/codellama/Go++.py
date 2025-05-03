# Test cases
T = int(input())
for t in range(T):
    N, L = map(int, input().split())
    G = set(input().split())
    B = input()
    
    # Check if B is in G
    if B in G:
        print("Case #" + str(t+1) + ": IMPOSSIBLE")
        continue
    
    # Find two programs that can produce all strings in G but not B
    for p1 in range(N):
        for p2 in range(p1, N):
            program1 = ""
            program2 = ""
            for i in range(L):
                if G[p1][i] == "0" and G[p2][i] == "1":
                    program1 += "0"
                    program2 += "1"
                elif G[p1][i] == "1" and G[p2][i] == "0":
                    program1 += "1"
                    program2 += "0"
                else:
                    program1 += "?"
                    program2 += "?"
            if all(s in G for s in [program1, program2]):
                print("Case #" + str(t+1) + ": " + program1 + " " + program2)
                break