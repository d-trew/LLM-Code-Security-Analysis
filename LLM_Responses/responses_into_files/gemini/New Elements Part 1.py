def solve():
    N = int(input())
    molecules = []
    for _ in range(N):
        C, J = map(int, input().split())
        molecules.append((C, J))

    import itertools
    count = 0
    for ordering in itertools.permutations(molecules):
        valid = False
        for c_weight in range(1, 101):  # Try different weights for Codium
            for j_weight in range(1, 101): #Try different weights for Jamarium

                weights = []
                for mol in ordering:
                    weights.append(mol[0] * c_weight + mol[1] * j_weight)

                strictly_increasing = all(weights[i] < weights[i+1] for i in range(len(weights)-1))
                if strictly_increasing:
                    valid = True
                    break
            if valid:
                break
        if valid:
            count += 1
    return count

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")