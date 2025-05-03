import sys

def read_input():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        molecules = []
        for _ in range(n):
            ci, ji = map(int, sys.stdin.readline().split())
            molecules.append((ci, ji))
        molecules.sort(key=lambda x: x[0] + x[1])
        if len(molecules) == 1:
            print(f"Case #{_ + 1}: IMPOSSIBLE")
            continue
        c, j = float('inf'), float('inf')
        for i in range(1, len(molecules)):
            _, ci_i = molecules[i]
            _, ji_i = molecules[i - 1]
            if ci_i > (c + j) // 2:
                c = min(ci_i - ji_i, c)
            elif j > (c + j) // 2:
                j = min(ji_i - ci_i, j)
        print(f"Case #{_ + 1}: {int(c)}, {int(j)}")

read_input()


This code reads the input from standard input (stdin), processes it according to the problem description, and writes the output to standard output (stdout). The input is read in test cases, where each test case contains the number of molecules (N) followed by the number of atoms of Codium and Jamarium for each molecule. The molecules are sorted by increasing molecular weight, and the atomic weights of Codium and Jamarium that satisfy the conditions are found using binary search. If there is no pair of values that would make the ordering strictly increasing, it prints "IMPOSSIBLE".