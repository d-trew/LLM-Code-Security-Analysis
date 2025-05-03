T, N, W = map(int, input().split())
score1, score2 = 0, 0
for _ in range(T):
    used = set()
    for i in range(N):
        A, B = map(int, input().split())
        C, D = map(int, input().split())
        if A not in used and B not in used:
            used.add(A)
            used.add(B)
            score1 += len(used) - 2
        used.add(C)
        used.add(D)
    result = int(input())
    if result == 1:
        score1 += 1
print(score1)