import math

T = int(input())

for case in range(1, T+1):
    N, Q = map(int, input().split())
    E = []
    S = []
    D = []
    for i in range(Q):
        E.append(list(map(int, input().split())))
        S.append(E[i][0])
        D.append(E[i][1])
        
    for i in range(N):
        if E[i][2] == -1:
            continue
        else:
            E[i][2] = math.ceil((E[i][2]/60)*10**6)
            
    for i in range(Q):
        D[i] = math.ceil((D[i]/60)*10**6)
        
    for i in range(N-1):
        if S[i+1] == -1:
            continue
        else:
            S[i+1] = math.ceil((S[i+1]/60)*10**6)
            
    print("Case #" + str(case) + ":", end="")
    
    for i in range(Q):
        if D[i] == -1:
            continue
        else:
            print(str(S[D[i]]) + " " + str(E[D[i]][2]) + " ", end="")