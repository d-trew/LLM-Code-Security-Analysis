import random
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    gophers = [0] * (N + 1)
    for _ in range(N):
        for i in range(18):
            if random.randint(0, 1):
                windmill = random.randint(0, 17)
                blades = random.randint(2, 18)
                for j in range(blades):
                    gophers[windmill] += 1
    print(sum(gophers))