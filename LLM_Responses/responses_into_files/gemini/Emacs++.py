def solve():
    K, Q = map(int, input().split())
    P = input()
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    Pi = list(map(int, input().split()))
    S = list(map(int, input().split()))
    E = list(map(int, input().split()))

    total_time = 0
    for j in range(Q):
        start = S[j] -1
        end = E[j] -1
        
        q_time = float('inf')

        #Try direct moves
        q_time = min(q_time, abs(end - start))

        #Try teleportations

        q_time = min(q_time,1)

        total_time += q_time

    return total_time

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")