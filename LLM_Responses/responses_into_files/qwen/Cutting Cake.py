from fractions import Fraction

def calculate_enjoyment(A, B, P, Q, R, S):
    return A * (P + R) / 2 + B * (Q + S) / 2

def min_difference(N, W, H, P, Q, R, S, patches):
    total_enjoyment = [0, 0]
    for X_i, Y_i, A_i, B_i in patches:
        area = calculate_enjoyment(A_i, B_i, P, Q, R, S)
        x1, y1 = X_i, Y_i
        x2, y2 = X_i + P, Y_i + Q
        x3, y3 = X_i + R, Y_i + S
        if x2 <= W:
            total_enjoyment[0] += area * (W - x2) / (x3 - x1)
            total_enjoyment[1] += area * (x2 - x1) / (x3 - x1)
    min_diff = float('inf')
    for i in range(W + 1):
        diff = abs(total_enjoyment[0] - sum(total_enjoyment[1:] - Fraction(i, W) * area for _, _, A_i, B_i, area in patches))
        if diff < min_diff:
            min_diff = diff
    return Fraction(min_diff).limit_denominator()

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        W = int(data[index + 1])
        H = int(data[index + 2])
        P = int(data[index + 3])
        Q = int(data[index + 4])
        R = int(data[index + 5])
        S = int(data[index + 6])
        index += 7
        
        patches = []
        for _ in range(N):
            X_i = int(data[index])
            Y_i = int(data[index + 1])
            A_i = int(data[index + 2])
            B_i = int(data[index + 3])
            area = calculate_enjoyment(A_i, B_i, P, Q, R, S)
            patches.append((X_i, Y_i, A_i, B_i, area))
            index += 4
        
        result = min_difference(N, W, H, P, Q, R, S, patches)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()