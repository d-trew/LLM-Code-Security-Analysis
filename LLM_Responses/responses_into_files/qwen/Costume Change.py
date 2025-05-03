def min_changes_to_special(n, grid):
    from collections import defaultdict

    def count_conflicts(grid):
        row_counts = [defaultdict(int) for _ in range(n)]
        col_counts = [defaultdict(int) for _ in range(n)]
        conflicts = 0

        for i in range(n):
            for j in range(n):
                abs_val = abs(grid[i][j])
                if row_counts[i][abs_val] > 0 or col_counts[j][abs_val] > 0:
                    conflicts += 1
                row_counts[i][abs_val] += 1
                col_counts[j][abs_val] += 1

        return conflicts

    def change_costume(i, j):
        grid[i][j] = -grid[i][j]

    min_changes = float('inf')

    for i in range(n):
        for j in range(n):
            original_value = grid[i][j]
            change_costume(i, j)
            current_conflicts = count_conflicts(grid)
            if current_conflicts < min_changes:
                min_changes = current_conflicts
            change_costume(i, j)  # Revert the change

    return min_changes

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        grid = []
        for _ in range(n):
            row = list(map(int, data[index:index + n]))
            index += n
            grid.append(row)
        
        min_changes = min_changes_to_special(n, grid)
        results.append(f"Case #{_ + 1}: {min_changes}")

    print("\n".join(results))

if __name__ == "__main__":
    main()