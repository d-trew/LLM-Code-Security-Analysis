T = int(input()) # read number of test cases
for i in range(1, T+1):
    N = int(input())
    lists = []
    for j in range(2*N-1):
        lists.append([int(x) for x in input().split()])
    
    # sort the 2*N-1 lists of soldiers' heights
    for l in lists:
        l.sort()
        
    # find the missing list by comparing pairs of rows and columns
    for r in range(N):
        row = []
        col = []
        for j in range(N):
            row.append(lists[2*r][j])
            col.append(lists[2*r+1][j])
        
        # check if the rows and columns are different
        if row != lists[2*r]:
            print("Case #{}: {}".format(i, " ".join([str(x) for x in row]))
            break
        elif col != lists[2*r+1]:
            print("Case #{}: {}".format(i, " ".join([str(x) for x in col]))
            break
    else:
        # if no missing list found, check the last two rows and columns
        row = []
        col = []
        for j in range(N):
            row.append(lists[-2][j])
            col.append(lists[2*N-1][j])
        
        # check if the rows and columns are different
        if row != lists[-2]:
            print("Case #{}: {}".format(i, " ".join([str(x) for x in row]))
        elif col != lists[2*N-1]:
            print("Case #{}: {}".format(i, " ".join([str(x) for x in col])