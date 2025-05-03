num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    columns = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        columns.append((x, y, h))
    
    # Sort the columns based on their heights (h) in descending order
    sorted_columns = sorted(columns, key=lambda col: col[2], reverse=True)
    
    # Initialize the output with the index of the first column
    result = [1]
    
    for i in range(1, N):
        # Check if the current column can be built without violating any rules
        for j in range(i-2, -1, -1):
            col_j = sorted_columns[j]
            col_k = sorted_columns[i]
            
            # If the two columns are not coplanar and not collinear, then they can form a roof
            if (col_j[:2] != col_k[:2]) and (col_j[0]*(col_k[1]-col_j[1])+col_j[1]*(col_k[0]-col_j[0]) != 0):
                result.append(i+1)
                break
    
    print("Case #{}: {}".format(case, " ".join(map(str, result)))<|im_sep|>