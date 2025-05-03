from collections import defaultdict

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    topics = [input().split() for _ in range(N)]
    first_words = set()
    second_words = set()
    fake_topics = 0
    for topic in topics:
        if topic[0] not in first_words and topic[1] not in second_words:
            first_words.add(topic[0])
            second_words.add(topic[1])
        else:
            fake_topics += 1
    print(f"Case #{i}: {fake_topics}")