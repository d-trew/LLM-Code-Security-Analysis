import random
T = int(input())

for t in range(T):
    U = int(input())
    records = []
    for i in range(104):
        Qi, Ri = input().split()
        if Qi == "-1":
            Mi = random.randint(1, U)
        else:
            Mi = int(Qi)
        Ni = random.randint(1, Mi)
        R_i = str(Ni)[::-1]
        records.append((Mi, Ri))
    D = ""
    for i in range(10):
        d_i = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        D += d_i
    print("Case #" + str(t+1) + ": " + D)