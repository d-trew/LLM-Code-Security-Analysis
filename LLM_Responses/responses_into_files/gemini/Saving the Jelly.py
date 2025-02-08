import itertools
import math

def solve():
    N = int(input())
    children = []
    for _ in range(N):
        children.append(list(map(int, input().split())))
    sweets = []
    for _ in range(N + 1):
        sweets.append(list(map(int, input().split())))

    for perm in itertools.permutations(range(N)):
        available_sweets = list(range(N + 1))
        result = []
        possible = True
        for child_index in perm:
            child_x, child_y = children[child_index]
            min_dist = float('inf')
            best_sweet = -1
            for sweet_index in available_sweets:
                sweet_x, sweet_y = sweets[sweet_index]
                dist = math.dist([child_x, child_y], [sweet_x, sweet_y])
                if dist < min_dist:
                    min_dist = dist
                    best_sweet = sweet_index
            
            if best_sweet == 0:
                possible = False
                break
            result.append((child_index + 1, best_sweet + 1))
            available_sweets.remove(best_sweet)

        if possible:
            return "POSSIBLE\n" + "\n".join(map(lambda x: str(x[0]) + " " + str(x[1]), result))
    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")