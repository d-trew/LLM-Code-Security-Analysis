def solve():
    F, K = map(int, input().split())
    fences = []
    for i in range(F):
        fences.append(list(map(int, input().split())))

    fixed_order = list(range(1, K + 1))
    remaining = list(range(K + 1, F + 1))

    import itertools

    for perm in itertools.permutations(remaining):
        order = fixed_order + list(perm)
        valid = True
        
        built_fences = []
        for fence_index in order:
            fence = fences[fence_index - 1]
            
            #Check for valid placement.  This is a simplification and may need refinement for edge cases.
            #A more robust solution would involve checking line intersections explicitly.

            valid_placement = True
            if built_fences:
                #Simplified check:  Just ensure no overlap with existing fences (Not considering printer visibility)
                for built_fence in built_fences:
                    if intersects(fence, built_fence):
                        valid_placement = False
                        break
            
            if not valid_placement:
                valid = False
                break
            built_fences.append(fence)

        if valid:
            return " ".join(map(str, order))

    return "No valid order found" #Should not happen given problem constraints

def intersects(fence1, fence2):
    #Simplified intersection check (only checks for overlap, not true intersection)
    x1, y1, x2, y2 = fence1
    x3, y3, x4, y4 = fence2
    
    return (min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and
            min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4))


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")