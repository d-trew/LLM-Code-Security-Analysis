import sys
from itertools import combinations

def solve(signs):
    west_signs = sorted([(d, s[0]) for s in signs])
    east_signs = sorted([(d, s[1]) for s in signs], reverse=True)
    n = len(west_signs)

    max_set_size = min(n, len(east_signs))
    result = [0] * (max_set_size + 1)
    for i in range(1, max_set_size + 1):
        comb = list(combinations(range(i), i))
        for c in comb:
            w_subseq = [west_signs[j] for j in c]
            e_subseq = [east_signs[j] for j in sorted(list(set(range(n)) - set(c)), reverse=True)[:i]]
            if all([w <= e for w, e in zip(w_subseq, e_subseq)]):
                result[i] += 1
    return result

T = int(sys.stdin.readline())
for _ in range(T):
    S = int(sys.stdin.readline())
    signs = [list(map(int, sys.stdin.readline().split())) for _ in range(S)]
    west_signs = sorted([(d, s[0]) for s in signs])
    east_signs = sorted([(d, s[1]) for s in signs], reverse=True)
    max_set_size = min(len(west_signs), len(east_signs))
    print("Case #{}: {} {}".format(_ + 1, max_set_size, sum(solve([(w, e) for w, e in zip(west_signs, east_signs)]))))


This Python program reads the number of test cases T from standard input and iterates through each test case. For each test case, it first reads the number of road signs S and then reads the positions, west-facing, and east-facing numbers for each sign. It sorts both sequences (west and east) by position. Then it calculates the maximum possible set size as min(number of west signs, number of east signs). After that, it uses itertools.combinations to find all combinations of signs for the calculated set size. For each combination, it checks if the west signs are less than or equal to the corresponding east signs. If so, it increments the count for that set size in the result array. Finally, it prints the result for each test case in the format specified in the problem description.