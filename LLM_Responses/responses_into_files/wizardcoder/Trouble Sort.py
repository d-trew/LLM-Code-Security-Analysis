T = int(input()) # number of test cases
for i in range(1, T+1):
    N = int(input())
    Vi = list(map(int, input().split()))
    swapped = True
    while swapped:
        swapped = False
        for j in range(N-2):
            if Vi[j] > Vi[j+1]:
                Vi[j], Vi[j+1] = Vi[j+1], Vi[j]
                swapped = True
    for k in range(N-2):
        if Vi[k] > Vi[k+1]:
            print("Case #{}: {}".format(i, k))
            break
    else:
        print("Case #{}: OK".format(i))