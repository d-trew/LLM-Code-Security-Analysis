import math

def calculate_distance(d1, d2, r):
    angle = abs(d1 - d2) % 360
    chord_length = 2 * r * math.sin(math.radians(angle / 2))
    return chord_length + r * 2

def find_k_longest_cords(N, R, K, points):
    distances = []
    for i in range(N):
        for j in range(i + 1, N):
            distance = calculate_distance(points[i][0], points[j][0], R) + points[i][1] + points[j][1]
            distances.append(distance)
    
    distances.sort(reverse=True)
    return distances[:K]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for t in range(T):
        N = int(data[index])
        R = float(data[index + 1])
        K = int(data[index + 2])
        points = []
        
        index += 3
        for _ in range(N):
            d = float(data[index])
            l = float(data[index + 1])
            points.append((d, l))
            index += 2
        
        result = find_k_longest_cords(N, R, K, points)
        results.append(f"Case #{t+1}: {' '.join(map(str, result))}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()