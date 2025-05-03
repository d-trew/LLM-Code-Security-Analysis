T = int(input())
for _ in range(T):
    Nmax, M, R = map(int, input().split())
    for _ in range(R):
        A, B = map(int, input().split())
        print(sum(max(abs(Xi-A), abs(Yi-B)) for Xi, Yi in [list(map(int, input().split())) for _ in range(Nmax)]))
    print('READY')
    for _ in range(R):
        C, D = map(int, input().split())
        print(sum(max(abs(Xi-C), abs(Yi-D)) for Xi, Yi in [list(map(int, input().split())) for _ in range(Nmax)]))