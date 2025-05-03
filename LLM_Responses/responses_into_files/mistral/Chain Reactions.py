from itertools import permutations
import sys
input = sys.stdin.readline

def fun(modules):
    fun_factors = [0] * len(modules)
    visited = set()

    def dfs(i, fun):
        if i in visited or modules[i] == -1:
            return 0
        visited.add(i)
        fun[i] = max(fun[i], fun)
        for j in range(len(modules)):
            if modules[j][i] != -1 and j not in visited:
                dfs(modules[j][i], fun[i])
        return fun[i]

    for i, f in enumerate(modules[0]):
        if f == 0:
            continue
        fun[i] = dfs(i, f)
        visited.clear()
    return sum(fun)

T = int(input())
for _ in range(T):
    N = int(input())
    modules = [[0]*N for _ in range(N)]
    for i, line in enumerate(map(int, input().split())):
        modules[i][i] = line
    for i, line in enumerate(map(int, input().split())):
        modules[i][line-1] = -1 if line == 0 else line-1
    print("Case #{}: {}".format(_+1, fun(modules)))


This Python code takes as input the number of test cases T, followed by the description for each test case. Each test case consists of the number of modules N, their fun factors, and their pointing relationships. The program computes the maximum fun Wile can get by manually triggering the initiators in the best possible order using dynamic programming and depth-first search. It then prints the result for each test case.