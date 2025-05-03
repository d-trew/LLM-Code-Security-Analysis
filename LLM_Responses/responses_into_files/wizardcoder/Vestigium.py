import sys

def get_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace

def count_repeated_rows(matrix):
    rows_with_repeats = []
    cols_with_repeats = []
    seen_rows = set()
    seen_cols = set()
    
    for i in range(len(matrix)):
        row_set = set([matrix[i][j] for j in range(len(matrix))])
        col_set = set([matrix[j][i] for j in range(len(matrix)])
        
        if len(row_set) != len(matrix):
            rows_with_repeats.append(i+1)
            
        if len(col_set) != len(matrix):
            cols_with_repeats.append(i+1)
    
    return (rows_with_repeats, cols_with_repeats)

def is_natural_latin_square(matrix):
    rows_with_repeats, cols_with_repeats = count_repeated_rows(matrix)
    return len(rows_with_repeats) == 0 and len(cols_with_repeats) == 0
    
def main():
    T = int(input())
    
    for i in range(1, T+1):
        N = int(input())
        
        matrix = []
        for _ in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
            
        trace = get_trace(matrix)
        rows_with_repeats, cols_with_repeats = count_repeated_rows(matrix)
        
        if is_natural_latin_square(matrix):
            print("Case #%d: %d 0 0" % (i, trace))
        else:
            print("Case #%d: %d %d %d" % (i, trace, len(rows_with_repeats), len(cols_with_repeats)))
        
if __name__ == "__main__":
    main()