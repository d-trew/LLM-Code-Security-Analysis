def min_time_to_get_picture(X, Y, M):
    px, py = 0, 0
    for move in M:
        if move == 'N':
            py += 1
        elif move == 'S':
            py -= 1
        elif move == 'E':
            px += 1
        elif move == 'W':
            px -= 1
        if abs(px) <= X and abs(py) <= Y:
            return M.index(move) + 1
    return "IMPOSSIBLE"

def solve():
    T = int(input())
    results = []
    for _ in range(T):
        X, Y, M = input().split()
        X, Y = int(X), int(Y)
        result = min_time_to_get_picture(X, Y, M)
        results.append(result)
    for i, result in enumerate(results, 1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    solve()