import sys

def count_googlements(g):
    count = {int(digit): 0 for digit in g}
    for digit in g:
        count[int(digit] += 1
    return sum([count[i]*2**(9-i) for i in range(1, 10)] + [count[0])