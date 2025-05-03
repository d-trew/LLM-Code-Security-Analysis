import sys

def solve(candj):
    c = candj[0].replace("?", "0")
    j = candj[1].replace("?", "0")
    c_nums = list(map(int, c))
    j_nums = list(map(int, j))
    min_abs_diff = abs(c_nums[-1] - j_nums[-1])
    for i in range(len(c_nums) - 2):
        diff = abs(c_nums[i] - j_nums[i])
        if diff < min_abs_diff:
            min_abs_diff = diff
    return "Case #" + str(case_number) + ": " + c.replace("?", str(c_nums[-1])) + " " + j.replace("?", str(j_nums[-1]))

if __name__ == '__main__':
    case_number = 1
    t = int(input())
    for _ in range(t):
        candj = input().split()
        print(solve(candj))
        case_number += 1