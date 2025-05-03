def max_points(mood_string):
    n = len(mood_string)
    points = 0
    request_queue = []
    
    for i in range(n):
        mood = mood_string[i]
        
        if request_queue:
            last_request = request_queue[-1]
            if last_request == mood:
                points += 5
            else:
                points += 5
            request_queue.pop()
            
        if mood == 'C':
            request_queue.append('C')
        elif mood == 'J':
            request_queue.append('J')
    
    return points

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        mood_string = data[i]
        result = max_points(mood_string)
        results.append(f"Case #{i}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()