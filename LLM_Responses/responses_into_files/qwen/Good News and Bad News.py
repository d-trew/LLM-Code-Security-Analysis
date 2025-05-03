T = int(input())
for _ in range(T):
    F, P = map(int, input().split())
    news_values = [0] * (F + 1)
    for _ in range(P):
        A, B = map(int, input().split())
        if B > A:
            A, B = B, A
        news_values[A] += int(input())
        news_values[B] -= int(input())
    if any(sum(map(abs, news_values[i:]))) % (2 * F) != 0:
        print(f"Case # {_ + 1}: IMPOSSIBLE")
    else:
        for _ in range(P):
            A, B = map(int, input().split())
            if B > A:
                A, B = B, A
            news_values[A] -= int(input())
            news_values[B] += int(input())
        print(f"Case # {_ + 1}: {' '.join(map(str, news_values[1:]))}")