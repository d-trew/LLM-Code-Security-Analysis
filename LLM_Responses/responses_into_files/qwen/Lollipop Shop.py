import sys

input = sys.stdin.read
data = input().split()

index = 0

def read_int():
    global index
    result = int(data[index])
    index += 1
    return result

T = read_int()
for _ in range(T):
    N = read_int()
    sold = [False] * N
    for _ in range(N):
        D = read_int()
        likes = set(data[index:index + D])
        index += D
        for flavor in likes:
            if not sold[int(flavor)]:
                print(int(flavor))
                sold[int(flavor)] = True
                break
        else:
            print(-1)