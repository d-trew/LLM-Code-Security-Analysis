import sys

def solve(n_test_cases):
    for t in range(1, n_test_cases + 1):
        n = int(input())
        molecules = []
        for i in range(n):
            ci, ji = map(int, input().split())
            molecules.append((ci, ji))
        valid_orderings = 0
        for i in range(len(molecules)):
            ci, ji = molecules[i]
            for j in range(i + 1, len(molecules)):
                cj, jj = molecules[j]
                if (ci + cj) % 2 == 0 and (ji + jj) % 2 == 0:
                    valid_orderings += 1
        print("Case #{}".format(t))
        print(valid_orderings)

if __name__ == "__main__":
    T = int(input())
    solve(T)