T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    sum_squares_A = sum(i**2 for i in A)
    if (sum_A ** 2 == sum_squares_A):
        print("Case #{}: {}".format(_, "IMPOSSIBLE"))
    else:
        for x in range(-10**18, 10**18+1):
            B = A + [x]
            sum_B = sum(B)
            sum_squares_B = sum(i**2 for i in B)
            if (sum_B ** 2 == sum_squares_B):
                print("Case #{}: {}".format(_, " ".join(map(str, B))))
                break
        else:
            print("Case #{}: IMPOSSIBLE".format(_))