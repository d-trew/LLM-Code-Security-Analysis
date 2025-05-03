from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        prereqs = [0]*N
        courses = []
        for _ in range(N):
            line = list(map(int, input().split()))[1:]
            if len(line) == 2:  # basic course
                prereqs[line[1]-1] += 1
            else:  # advanced course
                courses.append((line[0], line[1]))
        cool_words = [input().strip() for _ in range(M)]
        
        q = deque([i for i, v in enumerate(prereqs) if v == 0])
        dp = [[0]*(N+1) for _ in range(N+1)]
        dp[0][0] = 1
        for x in range(1, N+1):
            dp[x] = [sum([dp[y-1][x-1]*26**i if y>0 else 0 for i, y in enumerate(courses)])%1000000007 for _ in range(N+1)]
        
        res = [[0.0]*(M+1) for _ in range(N+1)]
        total_cases = 6**N % 1000000007
        for x in range(1, N+1):
            for y in range(min(x, M), -1, -1):
                if y + 1 <= M:
                    res[x][y] = (res[x-1][y]*26 % 1000000007 + dp[x-1][y+1]*courses[y])%1000000007
                if y == M:
                    res[x][y] = (res[x][y] + 1) % 1000000007
        
        print('Case #{}:'.format(t+1), end=' ')
        for word in cool_words:
            cnt = 0
            lw, tw = len(word), total_cases
            if lw <= N:
                for i in range(lw):
                    cnt += res[i][courses.index(N-lw+1)]*tw**(N-i) % 1000000007
                print('{:.6f}'.format((cnt/total_cases)*100), end=' ')
            else:
                print('{}'.format(0.0), end=' ')
        print()
        
solve()