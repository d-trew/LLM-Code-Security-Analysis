T = int(input())
for t in range(1, T + 1):
    N, Q = map(int, input().split())
    answers = [input() for _ in range(N)]
    scores = list(map(int, input().split()))
    max_score = sum(scores) / len(scores)
    answer = ''
    for i in range(Q):
        t_count = 0
        f_count = 0
        for j in range(N):
            if answers[j][i] == 'T':
                t_count += 1
            else:
                f_count += 1
        if t_count > f_count:
            answer += 'T'
        elif f_count > t_count:
            answer += 'F'
        else:
            answer += 'T' if sum(1 for a in answers if a[i] == 'T') >= N // 2 else 'F'
    print(f"Case #{t}: {answer} {max_score:.0f}/{Q}")