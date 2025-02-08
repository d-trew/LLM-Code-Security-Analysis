def solve():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        N = int(input())
        low = A + 1
        high = B
        for _ in range(N):
            guess = (low + high) // 2
            print(guess)
            result = input()
            if result == "CORRECT":
                break
            elif result == "TOO_SMALL":
                low = guess + 1
            elif result == "TOO_BIG":
                high = guess - 1
            else:
                return

solve()