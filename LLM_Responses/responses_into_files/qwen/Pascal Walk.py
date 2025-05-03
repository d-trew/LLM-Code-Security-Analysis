def generate_pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def find_pascal_walk(n, max_steps=500):
    pascal_triangle = generate_pascal_triangle(max_steps)
    walk = [(1, 1)]
    current_sum = 1
    for i in range(2, max_steps + 1):
        if current_sum >= n:
            break
        for j in range(1, i):
            value = pascal_triangle[i-1][j]
            if current_sum + value <= n:
                walk.append((i+1, j+1))
                current_sum += value
                break

    return walk[:n]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        walk = find_pascal_walk(N)
        results.append(f"Case #{_+1}:")
        for pos in walk:
            results.append(f"{pos[0]} {pos[1]}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()