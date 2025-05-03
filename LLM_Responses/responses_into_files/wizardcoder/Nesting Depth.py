import re

def solve(S):
    stack = []
    result = ''
    for i, c in enumerate(S):
        if c == '(':
            stack.append((c, i) if not stack else (stack[-1][0] + 1, max(stack[-1][1], i)) )
        elif c == ')':
            if not stack or stack[-1][0] % 2 == 1:
                result += '(' * (int(c)*2) + c
                continue
            while stack and stack[-1][0] < int(c):
                stack.pop()
            if not stack:
                result += '('*int(c)*2 + c
        else:
            depth = len(stack) * 2
            result += '('*depth + c + ')'*depth
    while stack:
        result += ')'*(stack[-1][0]-1) + ')'
        stack.pop()
    return result

def main():
    T = int(input())
    for i in range(1, T+1):
        S = input().strip()
        print("Case #%d: %s" % (i, solve(S))

if __name__ == "__main__":
    main()