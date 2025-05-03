import sys

T = int(input())
for i in range(1, T+1):
    N = int(input())
    A = []
    for _ in range(N):
        A.append([int(x) for x in input().split()])
    
    changed_count = 0
    for j in range(N):
        row_colors = set()
        col_colors = set()
        for k in range(N):
            if abs(A[j][k]) not in row_colors and A[j][k] > 0:
                row_colors.add(abs(A[j][k]) * (-1 if A[j][k] < 0 else 1) * -1)
            elif abs(A[j][k]) in row_colors and A[j][k] < 0:
                changed_count += 1
            
            if k not in col_colors and A[j][k] > 0:
                col_colors.add(abs(A[j][k]))
            elif k in col_colors and A[j][k] < 0:
                changed_count += 1
    
    print("Case #{}: {}".format(i, changed_count))