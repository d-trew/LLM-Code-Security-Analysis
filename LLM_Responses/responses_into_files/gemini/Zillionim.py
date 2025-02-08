T, W = map(int, input().split())

wins = 0

for _ in range(T):
    while True:
        P = int(input())
        if P == -2 or P == -3:
            break
        elif P == -1:
            exit()
        else:
            if (10**12 - P + 1) % 1010 == 0:
                Q = (10**12 - (10**10 * ((10**12-P+1)//1010)) )+1
            else:
                Q = 1
            print(Q)

    if P == -2:
        wins += 1

if wins >= W:
    exit(0)
else:
    exit(1)