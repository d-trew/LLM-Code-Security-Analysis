import sys
input = sys.stdin.read().splitlines()
T = int(input[0])
for i in range(1, T + 1):
    N = int(input[i])
    if N % 10 == 0:
        print("Case #" + str(i) + ": " + str(N // 10))
    elif N % 100 == 0:
        print("Case #" + str(i) + ": " + str(N // 100))
    elif N % 1000 == 0:
        print("Case #" + str(i) + ": " + str(N // 1000))
    else:
        print("Case #" + str(i) + ": " + str(N))