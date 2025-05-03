import sys
input = sys.stdin.readline

T, Nmax, M, R = map(int, input().split())
for _ in range(T):
    Xi, Yi = map(int, input().split())
    for _ in range(R):
        A, B = map(int, input().split())
        print(max(abs(A - Xi), abs(B - Yi)))
    print("READY")
    for _ in range(R):
        C, D = map(int, input().split())
        print(max(abs(C + M - Xi), abs(D + M - Yi)))