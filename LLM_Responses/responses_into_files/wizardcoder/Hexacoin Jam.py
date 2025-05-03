def main():
    T = int(input())
    for i in range(1, T+1):
        N, D = map(int, input().split())
        S, E = input(), input()
        L = [input() for _ in range(N)]
        count = 0
        total = 0
        for j in range(2**D):
            if all(S <= hex(j)[-1] < E for j in range(N)):
                count += 1
            total += 1
        y, z = count, total
        print("Case #{}: {} {}".format(i, y/z))