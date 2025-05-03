import math

def solve(T):
    for i in range(T):
        N = int(input())
        lasers = []
        for j in range(N):
            xi, yi, xi_prime, yi_prime = map(int, input().split())
            lasers.append((xi, yi))
        count = 0
        for k in range(len(lasers)):
            if lasers[k][1] > 0 and lasers[k][1] < 1000:
                count += 1
        print("Case #" + str(i+1) + ": " + str((count-1)/N))