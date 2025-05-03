T = int(input())
for _ in range(T):
    N = int(input())
    P = input()
    case_num = _ + 1
    path = []
    x, y = 0, N-1
    while (x, y) != (N-1, 0):
        if P[y*2+1] == 'E' and x < N-1:
            path.append('E')
            x += 1
        elif P[y*2] == 'S' and y > 0:
            path.append('S')
            y -= 1
        else:
            if y > 0 and (P[(y-1)*2] != 'S' or P[y*2+1] != 'E'):
                path.append('S')
                y -= 1
            elif x < N-1 and (P[y*2+1] != 'E' or P[(x+1)*2] != 'S'):
                path.append('E')
                x += 1
    print(f"Case #{case_num}: {''.join(path)}")