def solve():
    N, P = map(int, input().split())
    recipe = []
    for _ in range(P):
        recipe.append(int(input()))
    packages = []
    for _ in range(P):
        packages.append(list(map(int, input().split())))

    max_kits = 0
    
    num_packages = len(packages[0])
    
    def check_kit(kit_indices, servings):
        for i in range(P):
            required = recipe[i] * servings
            available = packages[i][kit_indices[i]]
            if not (0.9 * required <= available <= 1.1 * required):
                return False
        return True

    def count_kits(current_indices, kits_formed):
        nonlocal max_kits
        if len(current_indices) == P:
            
            for servings in range(1,101): #check for possible servings
                if check_kit(current_indices, servings):
                    max_kits = max(max_kits, kits_formed + 1)
                    return
            return

        
        for i in range(num_packages):
            valid_index = True
            for j in range(len(current_indices)):
                if current_indices[j] == i:
                    valid_index = False
                    break
            if valid_index:
                count_kits(current_indices + [i], kits_formed)

    count_kits([],0)
    return max_kits


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")