import sys
input = sys.stdin.readlines

def solve(test_cases):
    for case in test_cases:
        b, m = map(int, case.split())
        if b * (b - 1) // 2 > m:
            print("Case #{}: IMPOSSIBLE".format(case.split()[0]))
        else:
            slides = [[0] * (b + 1) for _ in range(b + 1)]
            count = 0
            for i in range(1, b):
                for j in range(i + 2, b + 1):
                    if not slides[i][j - 1] and not slides[j][i]:
                        slides[i][j] = 1
                        slides[j][i] = 1
                        count += 1
                        if count == m:
                            break
            for i in range(len(slides)):
                print("Case #{}:".format(case.split()[0]))
                for j in range(len(slides)):
                    if j != i and slides[i][j]:
                        print(" {}".format('1' if j < i else '0'), end='')
                    else:
                        print('0', end='')
                print()

if __name__ == "__main__":
    test_cases = list(map(int, input()))
    solve(test_cases)


This program reads the number of test cases and then iterates through each test case. For each test case, it checks if the total number of possible slides is greater than the required number of slides, in which case it outputs "IMPOSSIBLE". If it's possible, it constructs a set of slides according to the given conditions and prints the solution for that test case. If multiple solutions are possible, any valid one can be outputted.