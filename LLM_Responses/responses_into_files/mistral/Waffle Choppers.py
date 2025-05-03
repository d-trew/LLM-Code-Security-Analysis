import sys
input = sys.stdin.readlines

def can_split(r, c, h, v):
    grid = [list(map(lambda x: '@' if x == '1' else '. ', line.strip())) for line in input(f"{r+c}\n").split("\n")]
    pieces = [[0] * (v + 1) for _ in range(h + 1)]

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            pieces[i][cell == '@'] += 1

    for i in range(1, h):
        if sum(pieces[i]) != sum(pieces[0]) or sum(pieces[-1]) != sum(pieces[0]):
            return False

    for j in range(1, v):
        if sum([pieces[i][j] for i in range(r)]) != sum([pieces[i][0] for i in range(r)]):
            return False

    return True

for _ in range(int(input().strip())):
    r, c, h, v = map(int, input().split())
    if can_split(r, c, h, v):
        print(f"Case #{_+1}: POSSIBLE")
    else:
        print(f"Case #{_+1}: IMPOSSIBLE")