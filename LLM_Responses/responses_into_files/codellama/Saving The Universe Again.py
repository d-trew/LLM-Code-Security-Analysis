import sys

def solve(d, p):
    if d >= len(p):
        return "IMPOSSIBLE"
    else:
        hacks = 0
        while d > 0:
            hacks += 1
            for i in range(len(p) - 1):
                if p[i] == "C" and p[i + 1] == "S":
                    p[i], p[i + 1] = p[i + 1], p[i]
                    d -= 2
                    break
        return hacks

t = int(sys.stdin.readline())
for _ in range(t):
    d, p = map(str, sys.stdin.readline().split())
    print("Case #" + str(_ + 1) + ": " + solve(int(d), p))