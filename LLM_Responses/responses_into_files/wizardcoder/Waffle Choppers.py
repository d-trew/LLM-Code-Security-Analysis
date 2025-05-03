def main():
    T = int(input())
    for i in range(1, T+1):
        R, C, H, V = map(int, input().split())
        grid = []
        for _ in range(R):
            row = list(input())
            grid.append(row)
        if (H+1)*(V+1) > R*C:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            chips_per_piece = 0
            for row in grid:
                for cell in row:
                    if cell == '@':
                        chips_per_piece += 1
            if chips_per_piece % (H+1) != 0 or chips_per_piece % (V+1) != 0:
                print("Case #{}: IMPOSSIBLE".format(i))
            else:
                print("Case #{}: POSSIBLE".format(i))

if __name__ == "__main__":
    main()