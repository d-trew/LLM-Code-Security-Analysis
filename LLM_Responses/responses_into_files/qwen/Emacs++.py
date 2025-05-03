from collections import deque

def calculate_time(K, P, L, R, Pi, S, E):
    time = [0] * (K + 1)
    for i in range(1, K + 1):
        if P[i - 1] == '(':
            time[i] = time[i - 1] + 1
        else:
            time[i] = time[i - 1] - 1
    
    total_time = 0
    for s, e in zip(S, E):
        if s <= e:
            total_time += min(e - s, abs(time[e - 1] - time[s - 1]))
        else:
            total_time += min(s - e, abs(time[s - 1] - time[e - 1])) + 1
    
    return total_time

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        K = int(data[index])
        Q = int(data[index + 1])
        P = data[index + 2]
        L = [int(x) for x in data[index + 3:index + 3 + K]]
        R = [int(x) for x in data[index + 3 + K:index + 3 + 2 * K]]
        Pi = [int(x) for x in data[index + 3 + 2 * K:index + 3 + 3 * K]]
        S = [int(x) - 1 for x in data[index + 3 + 3 * K:index + 3 + 3 * K + Q]]
        E = [int(x) - 1 for x in data[index + 3 + 3 * K + Q:index + 3 + 4 * K + Q]]
        
        index += 4 * K + Q
        
        result = calculate_time(K, P, L, R, Pi, S, E)
        results.append(result)
    
    for i, res in enumerate(results):
        print(f"Case #{i + 1}: {res}")

if __name__ == "__main__":
    main()