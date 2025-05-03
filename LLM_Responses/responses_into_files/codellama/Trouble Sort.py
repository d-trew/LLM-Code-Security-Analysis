# This Python 3 program was created by Code Jam

T = int(input())
for i in range(T):
    N = int(input())
    Vi = list(map(int, input().split()))
    if sorted(Vi) == Vi:
        print("Case #{}: OK".format(i+1))
    else:
        error_index = 0
        while error_index < N-1 and Vi[error_index] > Vi[error_index+1]:
            error_index += 1
        print("Case #{}: {}".format(i+1, error_index))