import sys
from itertools import combinations

def solve(data):
    n, r, o, y, g, b, v = data
    if max([r+o+y+g+b+v]) > n or not all((x == 0 for x in [o-g, v])):
        return "IMPOSSIBLE"

    stalls = list(range(n))
    unicorns = {1: r, 2: o, 3: y, 4: g, 5: b, 6: v}
    for i in range(n):
        for j in range(i+1, n):
            if any((unicorns[k] & (1 << (stalls[i] ^ stalls[j])) for k in unicorns):
                stalls[i], stalls[j] = stalls[j], stalls[i]

    return "".join(str(unicorns[k]) for k in sorted(unicorns.keys()))

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        data = list(map(int, sys.stdin.readline().split()))
        print("Case #{}: {}".format(_+1, solve(data)))

if __name__ == "__main__":
    main()


The program reads the number of test cases from the standard input and iterates through each test case. For each test case, it checks if the given data is valid (the total number of unicorns cannot exceed the number of stalls and all unicorns with orange and violet manes must not have any common neighbors). If the data is invalid, it returns "IMPOSSIBLE". Otherwise, it initializes a list of stalls and a dictionary representing the unicorns. It then iterates through each pair of stalls and checks if the unicorns at those stalls share any hair colors. If they do, it swaps their positions in the stall list to ensure that no two unicorns sharing common hair colors are neighbors. Finally, it returns a string representing the placements of the unicorns in the stalls.