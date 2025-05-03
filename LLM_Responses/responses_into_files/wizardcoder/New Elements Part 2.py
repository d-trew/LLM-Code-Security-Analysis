def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        molecules = []
        for j in range(N):
            Ci, J = map(int, input().split())
            molecules.append((Ci*2 + J, Ci, J))
        if all([molecules[k][0] < molecules[k+1][0] for k in range(len(molecules)-1)]):
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            c, j = min([(C, J) for C in range(1, 101) for J in range(1, 101) if not any((C*2 + J < molecules[k][0] and C >= molecules[k][1]) or (J*2 + C < molecules[k][0] and J >= molecules[k][2]) for k in range(len(molecules)-1)])
            print("Case #{}: {} {}".format(i, c))