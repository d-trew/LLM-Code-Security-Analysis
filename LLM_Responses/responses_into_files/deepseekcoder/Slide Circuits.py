Here is the Python code for your problem. It uses a disjoint set data structure to keep track of the connected components in the graph of buildings. The `find` method finds the root of a building, and the `union` method merges two sets if they are not already connected. In each operation, it checks which slide can be enabled without making any cycle or creating more than one circuit for a single building.


class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                xr, yr = yr, xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
            self.parent[yr] = xr
            self.size[xr] += self.size[yr]
        return xr != yr

    def get_sizes(self):
        return [self.size[i] for i in range(len(self.size)) if self.find(i) == i]

def solve():
    T = int(input().strip())
    for t in range(1, T+1):
        B, S, N = map(int, input().split())
        edges = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(S)]
        ops = [tuple(input().split() + ['0', '0']) for _ in range(N)]
        dsu = DSU(B)
        res = []
        for op, l, r, m in sorted((a[2], int(b), int(c), int(d)) for a, (b, c, d) in zip(['E']+['D']*(N-1), ops, edges)):
            if op == 'E':
                res.append('X' if not any(dsu.union(x%m, (x+1)%m) for x in range(l, r+1)) else '')
            elif dsu.find(edges[r][0]) != dsu.find(edges[r][1]):
                res[-1] = str(r+1) if not dsu.union(edges[r][0], edges[r][1]) else ''
        print('Case #{}:'.format(t), ' '.join(res))