import sys
input = sys.stdin.readline()
T = int(input)
for i in range(T):
    input = sys.stdin.readline()
    N, K = map(int, input.split())
    input = sys.stdin.readline()
    E = [int(x) for x in input.split()]
    if is_squary(E):
        print("Case #{}".format(i+1))
        print(*E)
    else:
        for j in range(K):
            E.append(randint(-10**18, 10**18))
            if is_squary(E):
                print("Case #{}".format(i+1))
                print(*E)
                break
        else:
            print("Case #{} IMPOSSIBLE".format(i+1))