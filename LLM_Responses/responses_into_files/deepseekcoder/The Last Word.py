def last_word(s):
    s = sorted(list(s))
    for i in range(len(s)-1, -1, -1):
        if i == 0 or (i > 0 and s[i-1] != s[i]):
            return ''.join(s[:i+1])
    return ''

t = int(input())
for case in range(1, t + 1):
    s = input()
    print('Case #{}: {}'.format(case, last_word(s)))