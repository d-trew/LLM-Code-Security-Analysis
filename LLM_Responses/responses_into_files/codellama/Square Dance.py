# Test case 1:
T = int(input())
for i in range(T):
    R, C = map(int, input().split())
    dancers = []
    for j in range(R):
        row = list(map(int, input().split()))
        dancers.append(row)
    interest_level = 0
    for j in range(C):
        for k in range(R):
            if dancers[k][j] != 0:
                interest_level += dancers[k][j]
    print("Case #" + str(i+1) + ": " + str(interest_level))