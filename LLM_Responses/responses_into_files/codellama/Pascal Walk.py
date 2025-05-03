import math

def pascal_walk(n):
    walk = [(1, 1)]
    for i in range(2, n+1):
        prev_row = walk[-1]
        for j in range(len(prev_row)):
            if j == 0:
                walk.append((i, j))
            else:
                walk.append((i, j + prev_row[j-1]))
    return walk

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        walk = pascal_walk(n)
        print("Case #" + str(i+1) + ":")
        for pos in walk:
            print(pos[0], pos[1])