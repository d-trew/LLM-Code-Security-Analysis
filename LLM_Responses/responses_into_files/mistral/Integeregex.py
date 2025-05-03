import re
import sys

def count_matches(a, b, regex):
    pattern = re.compile('^{}$'.format(regex))
    count = sum(1 for i in range(a, b+1) if pattern.fullmatch(str(i)))
    return count

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    regex = input()
    print('Case #{}: {}'.format(_ + 1, count_matches(a, b, regex)))