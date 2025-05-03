def min_copyright_cost(X, Y, S):
    min_cost = 0
    CJ = S.count('CJ')
    JC = S.count('JC')
    
    while CJ > 0 and X <= Y:
        min_cost += X
        S = S.replace('CJ', '?', 1)
        CJ -= 1
        
    while JC > 0 and X >= Y:
        min_cost += Y
        S = S.replace('JC', '?', 1)
        JC -= 1
    
    remaining = S.count('C') + S.count('J')
    return min_cost + 2 * X * remaining if X < 0 else min_cost + 2 * Y * remaining

T = int(input())
for t in range(1, T+1):
    X, Y, S = input().split()
    print("Case #{}: {}".format(t, min_copyright_cost(int(X), int(Y), S)))