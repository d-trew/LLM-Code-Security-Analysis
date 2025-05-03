def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        F = list(map(int, input().split()))
        P = list(map(int, input().split()))
        max_fun = 0
        visited = [False] * N
        for j in range(N):
            if not visited[j]:
                chain_fun = []
                current_module = j
                while P[current_module] != -1:
                    visited[current_module] = True
                    chain_fun.append(F[current_module])
                    current_module = P[current_module]
                max_fun += max(chain_fun)
        print("Case #%d: %d" % (i, max_fun))
main()