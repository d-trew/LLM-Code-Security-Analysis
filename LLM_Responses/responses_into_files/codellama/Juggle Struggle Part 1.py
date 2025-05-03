import math

def find_pairs(jugglers):
    pairs = []
    for i in range(len(jugglers)):
        for j in range(i+1, len(jugglers)):
            if abs(jugglers[i][0] - jugglers[j][0]) + abs(jugglers[i][1] - jugglers[j][1]) <= 3:
                pairs.append([i, j])
    return pairs

def is_magnificent(pairs):
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            if abs(pairs[i][0] - pairs[j][0]) + abs(pairs[i][1] - pairs[j][1]) <= 3:
                return False
    return True

def solve(test_cases):
    for test_case in range(test_cases):
        N = int(input())
        jugglers = []
        for i in range(N):
            x, y = map(int, input().split())
            jugglers.append([x, y])
        pairs = find_pairs(jugglers)
        if is_magnificent(pairs):
            print("Case #" + str(test_case+1) + ": " + " ".join(map(str, [pair[0] for pair in pairs])))
        else:
            print("Case #" + str(test_case+1) + ": IMPOSSIBLE")

if __name__ == '__main__':
    t = int(input())
    solve(t)