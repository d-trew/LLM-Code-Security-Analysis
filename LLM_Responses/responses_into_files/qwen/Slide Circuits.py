T = int(input())
for _ in range(T):
    B, S, N = map(int, input().split())
    enabled_slides = [False] * (S + 1)
    circuits = []
    for _ in range(N):
        op, L, R, M = input().split()
        L, R, M = map(int, (L, R, M))
        if op == 'E':
            for i in range(L - 1, R):
                if i % M == 0:
                    enabled_slides[i] = True
        elif op == 'D':
            for i in range(L - 1, R):
                if i % M == 0 and enabled_slides[i]:
                    enabled_slides[i] = False
        else:
            print('Invalid operation')
            break
    for i in range(1, B + 1):
        if all(enabled_slides[S * (j - 1) + i % S] for j in range(1, len(circuits) + 2)):
            circuits.append(i)
    result = []
    for _ in range(N):
        y = 'X'
        for i in range(S):
            if enabled_slides[i]:
                break
        else:
            continue
        print(f'Case #{_+1}: {y}')
        break
    else:
        for _ in range(N):
            for i in range(S):
                if not enabled_slides[i] and all(enabled_slides[S * (j - 1) + i % S] for j in range(1, len(circuits) + 2)):
                    print(f'Case #{_+1}: {i+1}')
                    break
            else:
                continue
        else:
            for _ in range(N):
                y = 'X'
                for i in range(S - 1, 0, -1):
                    if not enabled_slides[i]:
                        y = str(i + 1)
                        break
                print(f'Case #{_+1}: {y}')