from sys import stdout, flush

def readline_int_list():
    return list(map(int, input().split()))

def printline(lst):
    for i in lst:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    flush(stdout)

t, n, c = readline_int_list()
pen_usage = [[0] * n for _ in range(t)]
remaining_ink = [0] * n

for round_num in range(min(n * (n + 1) // 2, t)):
    printline([pen for pen in range(1, n+1)])
    ink_spent = readline_int_list()
    for i in range(t):
        if ink_spent[i] == 0:
            continue
        remaining_ink[pen_usage[i][-1]] -= 1
        pen_usage[i].append(pen_usage[i][-1])
        if remaining_ink[pen_usage[i][-1]] == 0:
            break

    successful = sum([remaining_ink[i] > 0 for i in range(n)]) >= n
    if not successful and round_num < min(n * (n + 1) // 2, t) - 1:
        printline([0] * t)
        continue

    chosen = [[] for _ in range(t)]
    for i in range(len(pen_usage)):
        if pen_usage[i]:
            chosen[i % 2].append(pen_usage[i][-1])
    printline([0] * (2 * t))
    printline(chosen)
    exit()