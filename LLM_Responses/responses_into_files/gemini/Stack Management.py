def solve():
    P = int(input())
    premade_stacks = []
    for _ in range(P):
        line = list(map(int, input().split()))
        premade_stacks.append(line[1:])

    T = int(input())
    for t in range(1, T + 1):
        N, C = map(int, input().split())
        P_indices = list(map(int, input().split()))
        stacks = [premade_stacks[i] for i in P_indices]

        
        def is_winnable(current_stacks):
            if all(len(stack) <= 1 for stack in current_stacks):
                return True

            for i in range(len(current_stacks)):
                if len(current_stacks[i]) > 0:
                    new_stacks = [list(s) for s in current_stacks]
                    new_stacks[i].pop(0)
                    if is_winnable(new_stacks):
                        return True
            return False

        result = "POSSIBLE" if is_winnable(stacks) else "IMPOSSIBLE"
        print(f"Case #{t}: {result}")

solve()