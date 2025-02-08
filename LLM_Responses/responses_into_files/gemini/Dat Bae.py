def solve():
    N, B, F = map(int, input().split())
    
    broken = []
    queries = []
    
    for i in range(min(F, N)):
        query = bin(i)[2:].zfill(N)
        queries.append(query)
        print(query)
        response = input()
        if response == '-1':
            return
        
        for j in range(N):
            if (i >> j) & 1:
                if len(response) != N - len(broken):
                    broken.append(j)
                    
    broken.sort()
    print(*broken)
    response = input()
    if response == '-1':
        return

T = int(input())
for _ in range(T):
    solve()