import re

def flip_pancakes(stack):
    count = 0
    for i in range(len(stack)):
        if stack[i] == '-':
            start = i
            break
    else:
        return 0

    end = len(stack) - 1
    while start <= end:
        if stack[start] == '-':
            count += 1
            group_size = end - start + 1
            stack[start:end+1] = ['+' for _ in range(group_size)]
            end -= group_size
        else:
            start += 1
    return count

def main():
    cases = int(input())
    for case in range(1, cases + 1):
        stack = input().strip()
        print("Case #{}: {}".format(case, flip_pancakes(stack)))

main()