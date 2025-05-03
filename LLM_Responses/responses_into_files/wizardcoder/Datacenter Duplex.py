def main():
    T = int(input())
    for t in range(1, T + 1):
        R, C = map(int, input().split())
        matrix = []
        for i in range(R):
            row = list(input())
            if not all(c.isalpha() and c.isupper() for c in row):
                raise ValueError("Invalid input")
            matrix.append(row)
        # Check if A cells are connected and B cells are connected
        a_connected, b_connected = check_connection(matrix)
        if not (a_connected and b_connected):
            print(f"Case #{t}: IMPOSSIBLE")
            continue
        # Build connections through diagonal adjacencies
        build_connections(matrix)
        # Check if the resulting matrix is valid
        a_connected, b_connected = check_connection(matrix)
        if not (a_connected and b_connected):
            raise ValueError("Invalid connection")
        print(f"Case #{t}: POSSIBLE")
        for row in matrix:
            print("".join(row))

def build_connections(matrix):
    # Helper function to find the diagonal connection pair with the most connections
    def count_connections(i, j):
        a = [(-1, -1), (-1, 0), (0, -1)]
        b = [(1, 0), (0, 1), (1, 1)]
        counts = []
        for di, dj in a + b:
            count = 0
            ni, nj = i + di, j + dj
            while 0 <= ni < R and 0 <= nj < C:
                if matrix[ni][nj] == "A":
                    break
                elif matrix[ni][nj] == "B":
                    count += 1
                    break
                ni, nj = ni + di, nj + dj
            counts.append(count)
        return max(counts)

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == "A" and not (matrix[i - 1][j] == "B" or matrix[i + 1][j] == "B" or matrix[i][j + 1] == "B"):
                max_count = count_connections(i, j)
                if max_count > 0:
                    for di, dj in [(max_count, -1), (-1, max_count)]:
                        ni, nj = i + di, j + dj
                        while 0 <= ni < R and 0 <= nj < C:
                            if matrix[ni][nj] == "A":
                                break
                            elif matrix[ni][nj] == "B" and count_connections(i, j) > 1:
                                matrix[ni][nj] = "/"
                                break
                            ni, nj = ni + di, nj + dj
            if matrix[i][j] == "B" and not (matrix[i - 1][j] == "A" or matrix[i + 1][j] == "A" or matrix[i][j + 1] == "A"):
                max_count = count_connections(i, j)
                if max_count > 0:
                    for di, dj in [(max_count, -1), (-1, max_count)]:
                        ni, nj = i + di, j + dj
                        while 0 <= ni < R and 0 <= nj < C:
                            if matrix[ni][nj] == "B":
                                break
                            elif matrix[ni][nj] == "A" and count_connections(i, j) > 1:
                                matrix[ni][nj] = "\\"
                                break
                            ni, nj = ni + di, nj + dj
    return matrix

def check_connection(matrix):
    # Helper function to check if A cells are connected and B cells are connected
    def dfs(i, j, visited, company):
        if not (0 <= i < R and 0 <= j < C) or visited[i][j] or matrix[i][j] != company:
            return False
        visited[i][j] = True
        for di, dj in [(-1, -1), (-1, 0), (0, -1)]:
            dfs(i + di, j + dj, visited, company)
        return all(visited)
    a_connected = dfs(0, 0, [[False] * C for _ in range(R)], "A")
    b_connected = dfs(0, 0, [[False] * C for _ in range(R)], "B")
    return a_connected and b_connected

if __name__ == "__main__":
    main()