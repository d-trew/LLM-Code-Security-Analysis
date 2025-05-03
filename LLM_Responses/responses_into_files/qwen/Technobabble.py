def max_faked_topics(N, topics):
    words = set()
    fake_count = 0

    for first, second in topics:
        if (first, second) not in words and first != second:
            words.add((first, second))
        else:
            fake_count += 1

    return fake_count

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    topics = [tuple(input().split()) for _ in range(N)]
    result = max_faked_topics(N, topics)
    print(f"Case #{case}: {result}")