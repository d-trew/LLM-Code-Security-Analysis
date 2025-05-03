import sys
input = sys.stdin.readlines

def build_megatower(towers):
    tower_dict = {}
    for i, tower in enumerate(towers):
        if tower not in tower_dict:
            tower_dict[tower] = [i]
        else:
            tower_dict[tower].append(i)

    for key in sorted(tower_dict.keys()):
        if len(tower_dict[key]) > 1:
            for i, idx in enumerate(tower_dict[key]):
                if idx != tower_dict[key][0]:
                    return "IMPOSSIBLE"

    megatower = sorted(list(set().union(*[tower_dict[tower] for tower in tower_dict])))[::-1]
    return "Case #{}: {}".format(test_case, ''.join(map(str, megatower)))

T = int(input()[0].strip())
for test_case in range(1, T+1):
    N = int(input()[test_case-1].strip())
    towers = [list(input()[test_case].strip().split()) for _ in range(N)]
    print("Case #{}:".format(test_case), build_megatower(towers)

This program reads the number of test cases, then for each test case, it reads the number of towers and their respective letters. It then builds a dictionary where the keys are the unique tower strings and the values are lists of indices in the original list of towers. It checks if any tower appears more than once, and if so, returns "IMPOSSIBLE". If no such towers exist, it constructs the megatower by concatenating all the contiguous groups of letters in sorted order and prints the result.