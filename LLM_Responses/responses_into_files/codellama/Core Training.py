test_cases = int(input())
for t in range(1, test_cases+1):
    N, K = map(int, input().split())
    U = float(input())
    Pi = list(map(float, input().split()))
    success_probability = 0
    for i in range(N):
        if Pi[i] + U <= 1:
            success_probability += Pi[i] * (Pi[i] + U)
        else:
            success_probability += Pi[i]
    print("Case #{} {}".format(t, success_probability))