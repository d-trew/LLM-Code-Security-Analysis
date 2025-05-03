from itertools import combinations

for t in range(int(input())):
    n = int(input())
    for a, b in combinations(range(1, min(n, 105)), 2):
        if str(a).count("4") == 0 and str(b).count("4") == 0 and a + b == n:
            print(f"Case #{t+1}: {a} {b}")
            break