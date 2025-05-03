import sys
input = sys.stdin.readlines
T = int(input().strip())

def valid_orderings(molecules):
    n = len(molecules)
    if n == 1:
        return 1

    max_codium, max_jamarium = float('inf'), float('inf')
    for mol in molecules:
        C, J = mol
        max_codium = min(max_codium, C)
        max_jamarium = min(max_jamarium, J)

    if max_codium == max_jamarium:
        return 0

    count = 0
    for codium in range(max_codium + 1):
        for jamarium in range(max_jamarium + 1):
            if all([mol[0] >= codium and mol[1] >= jamarium for mol in molecules]):
                count += 1
    return count

for _ in range(T):
    N = int(input().strip())
    molecules = []
    for _ in range(N):
        C, J = map(int, input().split())
        molecules.append((C, J))
    print("Case #{}: {}".format(_ + 1, valid_orderings(molecules)))