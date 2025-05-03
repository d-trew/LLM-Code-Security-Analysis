def solve(s):
    res = []
    stack = []
    for c in s:
        if c == '0':
            while len(stack) > int(c):
                res.append(')')
                stack.pop()
            res.append('(')
            stack.append(1)
        else:
            while len(stack) < int(c):
                res.append('(')
                stack.append(1)
            for _ in range(int(c)):
                res.append(')')
                stack.pop()
    return ''.join(res)

T = int(input())
for i in range(T):
    s = input()
    print(f"Case #{i+1}: {solve(s)}")