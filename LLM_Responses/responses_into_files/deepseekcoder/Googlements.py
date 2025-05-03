def count_googlements(s):
    if len(set(s)) == 1 and '0' in set(s):
        return 1
    elif len(set(s)) > 2 or int(''.join(sorted(s))) != int(''.join(s)):
        return max([count_googlements(str(i)[:-1])+1 for i in s if i != '0'] + [int(s)])
    else:
        return count_googlements(str(sum([int(i) for i in set(s)]))[0]) + 1

T = int(input())
for tc in range(1, T+1):
    s = input()
    print('Case #{}: {}'.format(tc, count_googlements(s)))