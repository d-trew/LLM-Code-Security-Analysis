t = int(input())
for i in range(t):
    s = input()
    score = 0
    for j in range(len(s)):
        if (j // 2) % 2 == 0:
            score += 10 if s[j] == 'C' else 5
        else:
            score += 10 if s[j] == 'J' else 5
    print('Case #{}: {}'.format(i+1, score))