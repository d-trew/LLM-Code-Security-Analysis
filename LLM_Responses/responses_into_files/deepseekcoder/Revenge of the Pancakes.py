def min_flips(s):
    flips = 0
    for i in range(len(s)):
        if s[i] == '-':
            flips += 1
            for j in range(i+1, len(s)):
                if s[j] == '+':
                    break
                else:
                    s[j] = '+' if s[j] == '-' else '-'
    return flips

T = int(input())
for t in range(1, T + 1):
    s = list(input().strip())
    print('Case #{}: {}'.format(t, min_flips(s)))