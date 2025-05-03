T = int(input())
for t in range(1, T+1):
    N = int(input())
    workers = []
    for _ in range(N):
        worker = [int(c) for c in input()]
        workers.append(worker)
    min_spent = 0
    for i in range(N):
        for j in range(N):
            if workers[i][j] == 1:
                all_known = True
                for k in range(N):
                    if k != i and workers[k][j] == 1:
                        all_known = False
                        break
                if not all_known:
                    min_spent += 1
    print(f"Case #{t}: {min_spent}")