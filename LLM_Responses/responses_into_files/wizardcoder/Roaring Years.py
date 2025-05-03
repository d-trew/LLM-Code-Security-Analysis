t = int(input()) # number of test cases
for i in range(1, t+1):
    y = int(input())
    z = y + 1
    found_roaring_year = False
    while not found_roaring_year:
        if str(z) == ''.join([str(j) for j in range(y+1, z)]): # check if the decimal writing of z is concatenation of two or more consecutive integers in increasing order and without leading zeroes
            print("Case #{}: {}".format(i, z))
            found_roaring_year = True
        else:
            z += 1
    
# Example input:
# 3
# 2021
# 2019
# 5678

# Output:
# Case #1: 2022
# Case #2: 2024
# Case #3: 5680