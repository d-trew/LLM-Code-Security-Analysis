# Test case 1:
T = int(input())
W = 6
for i in range(T):
    R = [0, 0, 0, 0, 0, 0]
    for j in range(W+1):
        print("Enter the number of rings of type", j+1, ": ")
        n = int(input())
        R[j] += n
    for j in range(6):
        if R[j] > 0:
            print("Odin has", R[j], "ring of type", j+1)
    print()