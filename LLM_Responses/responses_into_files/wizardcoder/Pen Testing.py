import sys
from collections import Counter

def readline_int_list():
    return map(int, input().split())

t, n, c = readline_int_list()
pens = [0] * n # initialize all pens to 0 units of ink
successes = 0
for i in range(t):
    for j in range(n):
        print(j+1)
        sys.stdout.flush()
        spent_ink = int(input())
        if spent_ink == 1: # pen still has ink left
            pens[j] -= 1
    min_ink = n
    max_ink = -1
    for j, ink in enumerate(pens):
        if ink > 0 and ink < min_ink:
            min_ink = ink
        elif ink > max_ink:
            max_ink = ink
    if min_ink + max_ink >= c:
        successes += 1
    print(min_ink, max_ink)
    sys.stdout.flush()
    if successes == t:
        break
print(0) # end of input
sys.exit() # avoid TLE error by exiting gracefully