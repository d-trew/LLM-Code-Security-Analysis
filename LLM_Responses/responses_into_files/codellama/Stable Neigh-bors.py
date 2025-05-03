from itertools import permutations

def is_valid(stalls):
    for i in range(len(stalls) - 1):
        if set(stalls[i:i+2]).intersection({'R', 'O', 'Y', 'G', 'B', 'V'}):
            return False
    return True

for t in range(int(input())):
    N = int(input())
    R, O, Y, G, B, V = map(int, input().split())
    stalls = ['R' * R + 'O' * O + 'Y' * Y + 'G' * G + 'B' * B + 'V' * V][0]
    for p in permutations(stalls):
        if is_valid(p):
            print(f"Case #{t+1}: {''.join(p)}")
            break
    else:
        print(f"Case #{t+1}: IMPOSSIBLE")