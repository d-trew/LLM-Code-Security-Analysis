import sys
sys.setrecursionlimit(10**6)
MOD = 100000007
def count_configurations(n, s, tunnels):
    def dfs(box, visited, cats):
        if box == n:
            return int(cats > 0 and all(visited))
        for i in range(1, n+1):
            if not visited[i] and (tunnels[i-1] == -1 or visited[tunnels[i-1]) and s[i-1] != 'C'):
                return dfs(box + 1, visited[:i] + [True] + visited[i+1:], cats | (s[i-1] == 'C') << (i-1))
        return 0
    return sum(dfs(1, [False]*n, i) for i in range(2**n)) % MOD

def main():
    t = int(input())
    for test_case in range(t):
        n = int(input())
        s = input()
        tunnels = list(map(int, input().split()))
        cats = 0
        for i in range(n):
            if s[i] == 'C':
                cats |= (1 << i)
        result = count_configurations(n, s, tunnels)
        print("Case #%d: %d" % (test_case+1, result))

if __name__ == "__main__":
    main()