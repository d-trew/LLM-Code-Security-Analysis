import sys

def solve():
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N, K = map(int, sys.stdin.readline().split())
        Ci = list(map(int, sys.stdin.readline().split()))
        Di = list(map(int, sys.stdin.readline().split()))

        # count the number of pairs (L, R) that will result in a fair fight
        count = 0
        for L in range(1, N+1):
            for R in range(L, N+1):
                if all(abs(Ci[i] - Di[i]) <= K for i in range(L, R+1)):
                    count += 1

        print("Case #{}".format(test_case), end=": ")
        print(count)