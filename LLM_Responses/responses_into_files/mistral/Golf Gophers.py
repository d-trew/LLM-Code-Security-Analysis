import random
from collections import deque

def main():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        windmills = [(i, j) for i in range(1, N + 1) for j in range(2, min(N+1, 18))]
        gophers = deque()
        gophers.extend([random.randint(0, len(windmills)-1) for _ in range(M)])

        for _ in range(N):
            windmill_idx = gophers.popleft()
            windmill = windmills.pop(windmill_idx % len(windmills))
            windmills.insert((windmill[0] - 1) % len(windmills), (windmill[0], windmill[1]-1))
            gophers.append(windmill_idx)

        print(*[(w[1] + 1) % w[0] for w in windmills])

if __name__ == "__main__":
    main()


This program reads the number of test cases, N and M (number of nights and maximum number of gophers). It then initializes a list of windmills with their respective number of blades. A deque is used to store the gophers' choices of windmill. The algorithm simulates each night by having each gopher choose a windmill uniformly at random, rotating it counterclockwise by one blade, and updating the list of windmills accordingly. Finally, it prints the number on each windmill's downward-pointing blade for each test case.