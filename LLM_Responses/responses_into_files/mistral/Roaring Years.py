import re

def is_roaring(y):
    y = str(y)
    for i in range(len(y)):
        for j in range(i+1, len(y)):
            if int(y[i:j+1]) != j - i + int(y[j]):
                return False
    return True

def next_roaring(y):
    y = int(y) + 1
    while True:
        if is_roaring(y):
            return y
        y += 1

T = int(input())
for _ in range(T):
    Y = int(input())
    print(f'Case #{_+1}: {next_roaring(Y)}')