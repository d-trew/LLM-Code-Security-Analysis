def solve(towers):
    tower_blocks = []
    for tower in towers:
        tower_blocks += list(tower)
    
    result = ""
    stack = [tower_blocks[0]]
    for block in tower_blocks[1:]:
        if block >= stack[-1]:
            stack.append(block)
        else:
            while len(stack) > 0 and stack[-1] > block:
                result += stack.pop()
            if not (len(stack) > 0 and stack[-1] == block):
                return "IMPOSSIBLE"
    while len(stack) > 0:
        result += stack.pop()
    
    for i in range(1, len(result)):
        if result[i-1] == result[i]:
            return "IMPOSSIBLE"
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    towers = [input() for _ in range(N)]
    print("Case #{}: {}".format(tc, solve(towers)))