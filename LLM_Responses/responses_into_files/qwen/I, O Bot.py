def min_power_to_warehouse(N, C, balls):
    balls.sort()
    total_power = 0
    left_index = 0
    right_index = N - 1
    
    while left_index <= right_index:
        if balls[left_index][1] == '0':
            left_distance = abs(balls[left_index][0])
            right_distance = abs(balls[right_index][0])
            if left_distance < right_distance:
                total_power += left_distance * C
                left_index += 1
            else:
                total_power += right_distance * C
                right_index -= 1
        else:
            left_distance = abs(balls[left_index][0])
            right_distance = abs(balls[right_index][0])
            if left_distance < right_distance:
                total_power += left_distance
                left_index += 1
            else:
                total_power += right_distance
                right_index -= 1
    
    return total_power

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        C = int(data[index + 1])
        balls = []
        index += 2
        
        for _ in range(N):
            X = int(data[index])
            S = data[index + 1]
            balls.append((X, S))
            index += 2
        
        result = min_power_to_warehouse(N, C, balls)
        results.append(f"Case #{len(results) + 1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()