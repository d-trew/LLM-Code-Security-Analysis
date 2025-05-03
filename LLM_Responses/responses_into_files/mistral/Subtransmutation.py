import sys
input = sys.stdin.readlines

def solve():
    for _ in range(int(input()[0])):
        n, a, b = map(int, input().split())
        u = list(map(int, input().split()))
        if sum(u) > (n+1)*b - a:
            print("IMPOSSIBLE")
        else:
            m = max(set(u)) + 1
            used = [0]*m
            for i in range(m):
                used[i] = min((used[i]+u[i]), n)
            for i in range(m-a, 0, -a):
                if i < b:
                    used[i] += used[i+a]
            for i, v in enumerate(used[:n]):
                if v < u[i]:
                    print("IMPOSSIBLE")
                    break
            else:
                print("Case #{}: {}".format(_+1, m))

solve()