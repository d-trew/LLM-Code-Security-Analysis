T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    N = int(input())
    P = None
    for _ in range(N):
        Q = int(input("Guess: "))
        if Q < A or Q > B:
            print("WRONG_ANSWER")
            break
        elif Q == P:
            print("CORRECT")
            break
        else:
            if Q < P:
                print("TOO_SMALL")
            else:
                print("TOO_BIG")