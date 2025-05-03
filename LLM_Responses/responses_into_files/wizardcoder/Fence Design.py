n = int(input()) # number of poles
for i in range(1, n+1): 
    x_i, y_i = map(int, input().split())
    poles[x_i][y_i] = True 
m = int(input()) # existing fences
p_k, q_k = list(map(int, input().split())) 
for j in range(m-1):
    p_j, q_j = map(int, input().split())
    for k in range(p_j, q_j+1):
        poles[x_i][y_i] = True 
    for l in range(q_k, p_k-1, -1):
        poles[x_i][y_i] = True 

max_fences = [] # list of new fences to add
count = 0
for i in range(n):
    for j in range(i+1, n):
        if not (poles[i][j] or poles[j][i]):
            max_fences.append((i, j))
            count += 1
print("Case #", i+1, ": ", count)
for fence in max_fences:
    print(fence[0], fence[1])