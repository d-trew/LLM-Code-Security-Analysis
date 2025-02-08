def solve():
    R, C, H, V = map(int, input().split())
    waffle = [input() for _ in range(R)]

    total_chips = sum(row.count('@') for row in waffle)
    if total_chips == 0:
        return "POSSIBLE"

    if total_chips % (H + 1) % (V + 1) != 0:
        return "IMPOSSIBLE"

    chips_per_piece = total_chips // (H + 1) // (V + 1)

    for i in range(1 << R):
        horizontal_cuts = []
        for j in range(R -1):
            if (i >> j) & 1:
                horizontal_cuts.append(j)

        if len(horizontal_cuts) != H:
            continue
        
        for k in range(1 << C):
            vertical_cuts = []
            for l in range(C - 1):
                if (k >> l) & 1:
                    vertical_cuts.append(l)

            if len(vertical_cuts) != V:
                continue

            valid = True
            
            h_cuts = sorted([-1] + horizontal_cuts + [R-1])
            v_cuts = sorted([-1] + vertical_cuts + [C-1])

            for r in range(len(h_cuts) - 1):
                for c in range(len(v_cuts) - 1):
                    count = 0
                    for row in range(h_cuts[r] + 1, h_cuts[r+1] + 1):
                        for col in range(v_cuts[c] + 1, v_cuts[c+1] + 1):
                            if waffle[row][col] == '@':
                                count += 1
                    if count != chips_per_piece:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return "POSSIBLE"

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")