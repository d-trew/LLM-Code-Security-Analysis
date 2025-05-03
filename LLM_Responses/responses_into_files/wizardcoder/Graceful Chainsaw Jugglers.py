num_cases = int(input())
for case in range(1, num_cases + 1):
    R, B = map(int, input().split())
    max_jugglers = 0
    for i in range(max(R,B) + 1):
        if i * (i - 1) <= min(R,B):
            max_jugglers = max(max_jugglers, i)
    print("Case #{}: {}".format(case, max_jugglers))