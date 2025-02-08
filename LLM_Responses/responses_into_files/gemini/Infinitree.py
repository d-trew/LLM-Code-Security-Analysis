def get_path(node_index, l, r):
    path = []
    color = 1
    path.append((1,color))
    current_index = 1
    while current_index != node_index:
        if current_index * 2 < node_index:
            current_index *=2
            color = l[color -1]
        else:
            current_index = current_index * 2 +1
            color = r[color -1]
        
        path.append((current_index, color))
    return path

def solve():
    n, a, b = map(int, input().split())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    path_a = get_path(a, l, r)
    path_b = get_path(b, l, r)

    
    i = len(path_a) -1
    j = len(path_b) -1

    while i >=0 and j >= 0 and path_a[i][0] == path_b[j][0]:
      i -=1
      j -=1

    return len(path_a) -1 + len(path_b) -1 -2*min(i,j)


t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")