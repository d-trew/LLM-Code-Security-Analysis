def find_missing_list(T, lists):
    results = []
    for t in range(T):
        N = int(lists[t*N][0])
        rows = [list(map(int, lists[t*N+i+1].split())) for i in range(N)]
        cols = [[int(lists[t*N+N+i][j]) for j in range(N)] for i in range(N)]

        missing_list = []
        if len(rows) < N:
            missing_list = list(set(range(1, 2501)) - set(sum(rows, [])))
        elif len(cols) < N:
            missing_list = list(set(range(1, 2501)) - set(sum(cols, [])))

        results.append(f"Case #{t+1}: {missing_list}")

    return '\n'.join(results)

# Example usage
input_data = """
2
3
1 2 3
4 5 6
7 8
9 10 11
12 13 14
15 16
"""
print(find_missing_list(2, input_data.strip().split('\n')))