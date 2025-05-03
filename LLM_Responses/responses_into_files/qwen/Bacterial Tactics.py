def can_place_colony(matrix, row, col, direction):
    if direction == 'H':
        for c in range(col + 1, len(matrix[0])):
            if matrix[row][c] != '.':
                return False
    elif direction == 'V':
        for r in range(row + 1, len(matrix)):
            if matrix[r][col] != '.':
                return False
    return True

def place_colony(matrix, row, col, direction):
    if direction == 'H':
        for c in range(col + 1, len(matrix[0])):
            matrix[row][c] = '#'
    elif direction == 'V':
        for r in range(row + 1, len(matrix)):
            matrix[r][col] = '#'

def is_valid_move(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '.':
                return True
    return False

def solve(matrix):
    rows, cols = len(matrix), len(matrix[0])
    becca_wins = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '.':
                temp_matrix = [row[:] for row in matrix]
                place_colony(temp_matrix, r, c, 'H')
                if not is_valid_move(temp_matrix):
                    becca_wins += 1
                temp_matrix = [row[:] for row in matrix]
                place_colony(temp_matrix, r, c, 'V')
                if not is_valid_move(temp_matrix):
                    becca_wins += 1

    return becca_wins

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        index += 2
        matrix = [list(data[index + r]) for r in range(R)]
        index += R

        result = solve(matrix)
        results.append(result)

    for i, res in enumerate(results, start=1):
        print(f"Case #{i}: {res}")

if __name__ == "__main__":
    main()