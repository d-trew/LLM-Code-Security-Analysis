def find_path(n, p):
    path = []
    i = 0
    while i < len(p):
        if p[i] == 'E':
            path.append('S')
            i += 1
        else:  # p[i] == 'S'
            j = i + 1
            while j < len(p) and p[j] == 'S':
                path.append('S')
                j += 1
            if j == len(p):
                break
            path.append('E')
            i = j + 1
    return "Case #{}: {}".format(n, "".join(path))

t = int(input().strip())
for i in range(1, t+1):
    n = int(input().strip())
    p = input().strip()
    print(find_path(i, p))