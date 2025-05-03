from typing import List

def is_omnicircumnavigation(points: List[List[int]]) -> str:
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if (points[j][0] * points[i][0] + points[j][1] * points[i][1] + points[j][2] * points[i][2]) == 1:
                return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        points = []
        for _ in range(N):
            X, Y, Z = map(int, data[index:index + 3])
            index += 3
            points.append([X / (X**2 + Y**2 + Z**2)**0.5, Y / (X**2 + Y**2 + Z**2)**0.5, Z / (X**2 + Y**2 + Z**2)**0.5])
        
        results.append(is_omnicircumnavigation(points))
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()