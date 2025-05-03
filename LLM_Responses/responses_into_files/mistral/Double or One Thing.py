import sys
from itertools import permutations, combinations
from operator import itemgetter

def get_perms(s):
    perms = set()
    for i in range(1, len(s) + 1):
        for perm in permutations(s, i):
            new_perm = ''.join(2 * c if c in perm else c for c in perm)
            perms.add(new_perm)
    return perms

def lexicographically_first(perms):
    return min(perms, key=itemgetter(0))

T = int(sys.stdin.readline())
for _ in range(1, T + 1):
    S = sys.stdin.readline().strip()
    perms = get_perms(S)
    print(f'Case #{_}: {lexicographically_first(perms)}')


This program reads the number of test cases from the input, then for each test case it reads a string S and calculates all possible strings that can be obtained by the described process. It uses permutations function from itertools module to generate all possible permutations of the characters in S with length 1 to len(S) + 1. For each permutation, it creates a new string where non-highlighted letters are appended once and highlighted letters are appended twice. Finally, it finds the lexicographically first string from the set of generated strings using min function with itemgetter as key to compare the strings alphabetically. The result is printed for each test case.