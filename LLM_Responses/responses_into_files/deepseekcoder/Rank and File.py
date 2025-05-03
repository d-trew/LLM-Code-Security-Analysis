def find_missing(n, lists):
    row = sorted([i for i in range(1, n+1)])
    col = []
    
    # Find the missing column
    for lst in lists:
        if len(lst) != n-1:
            return "Error: Invalid input"
        elif set(lst).issubset(col):  # If all elements of this list are already in col, skip it
            continue
        else:
            for i in range(n-1):  
                if lst[i] != row[i]:  # Find the missing element from the row
                    col = lst[:i] + [lst[i]] + lst[i:]  # Insert this missing element into the column list
                    break
    return "Case #{}: {}".format(n, ' '.join(map(str,col)))

T = int(input().strip())
for t in range(1, T+1):
    N = int(input().strip())
    lists = []
    for _ in range(2*N-1):
        lst = list(map(int, input().strip().split()))
        lists.append(lst)
    print(find_missing(t, lists))