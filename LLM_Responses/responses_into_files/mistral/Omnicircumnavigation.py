import math

def is_omnicircumnavigation(N, X, Y, Z):
    for i in range(N):
        if i == N-1:
            j = 0
        else:
            j = i+1
        v1 = (X[i], Y[i], Z[i])
        v2 = (X[j], Y[j], Z[j])
        dot_product = sum(a*b for a, b in zip(v1, v2))
        magnitude1 = math.sqrt(sum(x**2 for x in v1))
        magnitude2 = math.sqrt(sum(x**2 for x in v2))
        cosine_angle = dot_product / (magnitude1 * magnitude2)
        if abs(cosine_angle) > 0.9999:
            return "NO"
    return "YES"

T = int(input())
for t in range(1, T+1):
    N = int(input())
    X = [list(map(float, input().split())) for _ in range(N)]
    Y = [x[1] for x in X]
    Z = [x[2] for x in X]
    print("Case #{}: {}".format(t, is_omnicircumnavigation(N, X, Y, Z)))