import re

def min_diff(case):
    c, j = case
    diff = abs(int(c.replace("?", "0")) - int(j.replace("?", "0")))
    best_c = max(0, min(9, (10 + diff - int(j.replace("?", "0"))) // 2))
    best_j = max(0, min(9, (10 + diff - int(c.replace("?", "0"))) // 2))
    c_fill = re.sub("?", str(best_c), c)
    j_fill = re.sub("?", str(best_j), j)
    return f"Case #{case.split()[0]}: {c_fill} {j_fill}"

T = int(input())
for _ in range(T):
    case = input().split()
    print(min_diff(case))