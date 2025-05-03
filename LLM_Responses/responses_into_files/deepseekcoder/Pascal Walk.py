def pascal_walk(n):
    walk = [(1, 1)] # start from the first position in Pascal's triangle
    current_sum = 1
    while len(walk) < n and current_sum < n:
        r, k = walk[-1]
        if k == 1 or (r == k): # if we are at the beginning of a row or the last element in the row
            walk.append((r+1, 1)) # move to the next row's first position
        else:
            walk.append((r, k-1)) # otherwise, move left
        current_sum += r
    return walk[:n]

t = int(input().strip())
for i in range(1, t+1):
    n = int(input().strip())
    walk = pascal_walk(500 if 500 < n else n)
    print("Case #{}:".format(i))
    for r, k in walk:
        print(r, k)