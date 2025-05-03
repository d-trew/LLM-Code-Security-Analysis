from collections import defaultdict
import bisect

def count_orderings():
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        molecules = [tuple(map(int, input().split())) for _ in range(N)]
        molecules.sort()  # sort by Codium atoms count
        
        dp_codium = defaultdict(list)
        dp_jamarium = defaultdict(list)
        valid_orderings = 0
        
        for c, j in molecules:
            if not dp_codium[c] or dp_codium[c][-1] < j:  # new max weight
                dp_codium[c].append(j)
            else:  # find a valid pair to replace the last one
                idx = bisect.bisect_right(dp_codarium[c], j)
                dp_codium[c][idx] = j
                
            if not dp_jamarium[j] or dp_jamarium[j][-1] < c:  # new max weight
                dp_jamarium[j].append(c)
            else:  # find a valid pair to replace the last one
                idx = bisect.bisect_right(dp_jamarium[j], c)
                dp_jamarium[j][idx] = c
                
        for arr in dp_codium.values():
            valid_orderings += len(arr) - 1
        for arr in dp_jamarium.values():
            valid_orderings += len(arr) - 1
        
        print("Case #{}: {}".format(case, valid_orderings))

count_orderings()