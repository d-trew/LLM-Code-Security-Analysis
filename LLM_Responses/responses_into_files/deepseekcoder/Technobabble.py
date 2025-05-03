def max_fakes(topics):
    words = set()
    real_topics = set()
    fake_topics = set()
    
    for t in topics:
        w1, w2 = t.split(' ')
        if (w1 + ' ' + w2) not in fake_topics and (w2 + ' ' + w1) not in fake_topics:
            real_topics.add(t)
        else:
            fake_topics.add((w1, w2))
        words.add(w1)
        words.add(w2)
    
    for f in fake_topics:
        if f[0] not in words or f[1] not in words:
            continue
        else:
            real_topics.add(' '.join(f))
            
    return len(fake_topics - set([t for t in fake_topics if (t[1], t[0]) in fake_topics]))

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    topics = [input() for _ in range(N)]
    print('Case #{}: {}'.format(case, max_fakes(topics)))