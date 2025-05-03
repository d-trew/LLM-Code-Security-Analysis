T = int(input())
for _ in range(T):
    N = int(input())
    A = set()
    for _ in range(N):
        a = int(input())
        while a in A:
            a += 1
        A.add(a)
    B = set()
    for _ in range(N):
        b = int(input())
        while b in A | B:
            b += 1
        B.add(b)
    print(*A)
    for i, b in enumerate(B):
        if sum(A) > sum(B):
            print(b)
        else:
            print(i+1)