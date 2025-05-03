import sys
def solve(S):
    K = int(sys.stdin.readline())
    if K == 0:
        return "IMPOSSIBLE"
    count = 0
    for i in range(K, len(S)):
        if S[i] != S[i - K]:
            count += 1
    if count % 2 == 0:
        return count // 2
    else:
        return "IMPOSSIBLE"
for t in range(int(sys.stdin.readline())):
    S = sys.stdin.readline()
    print("Case #%d: %s" % (t + 1, solve(S)))