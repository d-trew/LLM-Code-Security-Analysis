T = int(input())
W = int(input())

for _ in range(T):
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 0
    R6 = 0
    
    for _ in range(W):
        query = int(input())
        
        if query % 263 == 0:
            R1 += query // 1
        elif query % 131 == 0:
            R2 += query // 2
        elif query % 87 == 0:
            R3 += query // 3
        elif query % 43 == 0:
            R4 += query // 4
        elif query % 29 == 0:
            R5 += query // 5
        else:
            R6 += query // 6
        
    print(R1, R2, R3, R4, R5, R6)