def check_latin_square(matrix):
    N = len(matrix)
    trace = sum(matrix[i][i] for i in range(N))
    rows_with_repeats = set()
    cols_with_repeats = set()

    for i in range(N):
        row = matrix[i]
        col = [matrix[j][i] for j in range(N)]
        if len(row) != len(set(row)):
            rows_with_repeats.add(i)
        if len(col) != len(set(col)):
            cols_with_repeats.add(i)

    return trace, len(rows_with_repeats), len(cols_with_repeats)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        matrix = [list(map(int, data[index + 1:index + N + 1])) for index in range(index + 1, index + N + 1)]
        trace, rows_with_repeats, cols_with_repeats = check_latin_square(matrix)
        results.append(f"Case #{_ + 1}: {trace} {rows_with_repeats} {cols_with_repeats}")
        index += N + 1
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()