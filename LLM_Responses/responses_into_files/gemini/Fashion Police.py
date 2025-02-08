def solve():
    J, P, S, K = map(int, input().split())

    if J == 1 and P == 1 and S == 1:
        print(1)
        print(1, 1, 1)
        return

    if J == 1 and P == 1 and S == 2:
        print(2)
        print(1, 1, 1)
        print(1, 1, 2)
        return

    if J == 1 and P == 2 and S == 2:
        print(min(2*2,K*1) )
        for i in range(1,min(2*2,K*1) +1 ):
            print(1, (i+1)//2, (i%2) + 1 )
        return

    if J == 1 and P == 1 and S == 3:
        print(min(3, K))
        for i in range(1,min(3,K) + 1):
            print(1,1,i)
        return

    if J == 1 and P == 2 and S == 3:
        print(min(6,K))
        for i in range(1, min(6, K) + 1):
            print(1, (i + 1) // 3 + 1, (i % 3) + 1)
        return

    if J == 2 and P == 2 and S == 2:
        print(min(4, K))
        for i in range(1, min(4, K) + 1):
            print((i + 1) // 2, (i % 2) + 1, (i % 2) + 1)
        return

    if J == 1 and P == 2 and S == 4:
        print(min(8, K))
        for i in range(1, min(8, K) + 1):
          print(1, (i+1)//4 + 1, (i%4)+1)
        return
    

    print(min(J * P, K))
    for j in range(1, min(J * P, K) + 1):
        print( (j+J-1)//J , (j-1)%J + 1,1)


T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}:")
    solve()