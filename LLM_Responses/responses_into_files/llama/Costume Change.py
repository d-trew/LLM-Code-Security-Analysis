T = int(input())
for _ in range(T):
    N = int(input())
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    count = 0
    for i in range(N):
        colors = set()
        materials = set()
        for j in range(N):
            color = abs(A[i][j]) // (A[i][j] // abs(A[i][j]))
            material = A[i][j] // abs(A[i][j])
            if color in colors or material in materials:
                count += 1
                break
            colors.add(color)
            materials.add(material)
    print(f"Case #{_+1}: {count}")