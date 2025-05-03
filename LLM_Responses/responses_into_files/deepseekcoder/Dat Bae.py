import sys
read = sys.stdin.buffer.readline

def read_ints():
    return list(map(int, read().split()))

T = int(read())
for _ in range(T):
    N, B, F = read_ints()
    broken_workers = set()
    for _ in range(F):
        line = read().strip().decode('utf-8')
        if len(broken_workers) < B:
            if all(c == '0' or c == '1' for c in line):
                continue
            else:
                print("Wrong Answer")
                break
        elif len(broken_workers) > B:
            print("Wrong Answer")
            break
        else:
            if all(c == '0' or c == '1' for c in line):
                continue
            else:
                print("Wrong Answer")
                break
    else:
        print(*sorted(broken_workers))

This Python script reads the number of test cases `T` from standard input. For each test case, it reads the number of workers `N`, the number of broken workers `B` and the maximum allowed calls to `TEST_STORE` function `F`. It then reads up to `F` lines of data from the judge, checking that all read bits are either '0' or '1'. If a line does not contain these characters or if more than `B` broken workers are found, it prints "Wrong Answer" and stops. Otherwise, it continues until all `F` calls have been made. Finally, it prints the IDs of the broken workers in sorted order.