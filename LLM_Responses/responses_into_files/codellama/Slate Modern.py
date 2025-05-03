import math
def main():
    T = int(input())
    for i in range(T):
        R, C, N, D = map(int, input().split())
        grid = [[0]*C for _ in range(R)]
        for j in range(N):
            Ri, Ci, Bi = map(int, input().split())
            grid[Ri-1][Ci-1] = Bi
        if is_possible(grid, R, C, D) == True:
            print("Case #" + str(i+1) + ": " + str(max_sum(grid)))
        else:
            print("Case #" + str(i+1) + ": IMPOSSIBLE")
def max_sum(grid):
    result = 0
    for row in grid:
        result += sum(row) % (109+7)
    return result
def is_possible(grid, R, C, D):
    for i in range(R-1):
        for j in range(C-1):
            if abs(grid[i][j] - grid[i+1][j]) > D or abs(grid[i][j] - grid[i][j+1]) > D:
                return False
    return True