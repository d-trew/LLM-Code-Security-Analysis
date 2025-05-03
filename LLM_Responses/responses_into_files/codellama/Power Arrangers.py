import sys
input = sys.stdin.readline

# read input
T, F = map(int, input().split())

# process test cases
for t in range(T):
    # initialize variables
    sets = []
    figures = 0
    missing_set = -1

    # read number of sets and figures per set
    N, M = map(int, input().split())

    # process each set
    for i in range(N):
        # read the letters for each figure in the current set
        letters = list(map(str, input().split()))

        # add the letters to the corresponding sets
        sets.append(letters)

        # update the total number of figures
        figures += M

    # check if any set is missing
    for i in range(N):
        # check if the current set has been selected as the missing set
        if not all(letter in sets[i] for letter in "ABCDE"):
            missing_set = i
            break

    # print the answer
    if missing_set != -1:
        print(missing_set)
    else:
        print("none")