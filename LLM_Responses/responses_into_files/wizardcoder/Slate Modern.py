import sys
from collections import defaultdict

def prime_109():
    return 10**6+7

def main():
    T = int(input())
    
    for i in range(T):
        R, C, N, D = map(int, input().split())
        
        grid = defaultdict(lambda: -1)
        
        for _ in range(N):
            r, c, b = map(int, input().split())
            grid[(r,c)] = b
            
        possible_values = set()
        for i in range(R+1):
            for j in range(C+1):
                if grid[i,j] == -1:
                    neighbor_brightnesses = [grid.get((i-1,j), 0) % D, grid.get((i+1,j), 0) % D, grid.get((i,j-1), 0) % D, grid.get((i,j+1), 0) % D]
                    possible_values |= set(range(min(neighbor_brightnesses)-D, max(neighbor_brightnesses)+D+1))
        
        if len(possible_values) > R*C:
            print("Case #%d: IMPOSSIBLE" % (i+1)
        else:
            max_sum = sum([x for x in possible_values]) % prime_109()
            print("Case #%d: %d" % (i+1, max_sum))
        
if __name__ == "__main__":
    main()