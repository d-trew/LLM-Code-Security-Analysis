T = int(input())
for t in range(1, T+1):
    N = int(input())
    towers = [input() for _ in range(N)]
    megatower = []
    used_letters = set()
    for tower in towers:
        last_letter = None
        for block in tower:
            if block not in used_letters:
                if block != last_letter:
                    megatower.append(block)
                    used_letters.add(block)
                else:
                    break
            last_letter = block
    if len(megatower) == N * 10:
        print(f"Case #{t}: {''.join(megatower)}")
    else:
        print(f"Case #{t}: IMPOSSIBLE")