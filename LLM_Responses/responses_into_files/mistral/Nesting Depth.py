from collections import deque

def solve(s):
    nesting = deque()
    depth = [0] * (len(s) + 1)

    for i, c in enumerate(s):
        if c == '(':
            nesting.append((i, 1))
            depth[i+1] = max(depth[i], 1)
        elif c == ')':
            last = nesting.pop()
            if not nesting or last[1] - depth[last[0]] != 1:
                return "Invalid"
            depth[last[0]] -= 1

    if nesting:
        return "Invalid"

    res, cnt = "", 0
    for i, c in enumerate(s):
        if c.isdigit():
            cnt += int(c)
            res += str(cnt) * depth[i]
        elif cnt > 0:
            res += '(' * cnt + c + ')' * cnt
            cnt = 0
    return res

T = int(input())
for _ in range(T):
    print(f"Case #{_ + 1}: {solve(input())}")