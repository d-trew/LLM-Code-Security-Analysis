def sort_arrays(P, S, K, N, arrays):
    permutations = []
    for i in range(1, P + 1):
        perm = list(range(N))
        random.shuffle(perm)
        permutations.append(perm)

    results = []
    for array in arrays:
        sorted_array = sorted(array)
        instructions = []
        for _ in range(S):
            current_perm = permutations[random.randint(0, P - 1)]
            if array == sorted_array:
                break
            applied_perm = [array[current_perm[i] - 1] for i in range(N)]
            array = applied_perm
            instructions.append(current_perm)
        results.append((instructions, array))

    return results

# Example usage
import random

P = 20
S = 450
K = 30
N = 50
arrays = [[random.randint(1, 1000) for _ in range(N)] for _ in range(K)]

sorted_results = sort_arrays(P, S, K, N, arrays)
for i, (instructions, sorted_array) in enumerate(sorted_results):
    print(f"Case #{i + 1}:")
    print(len(instructions))
    for perm in instructions:
        print(" ".join(map(str, perm)))