import math

def max_rounded_percentage(N, L, C):
    total_people = N - sum(C)
    remaining_languages = L - len(C)
    if remaining_languages == 0:
        return round((sum(C) * 100) / N)
    
    max_percentage = 0
    for i in range(remaining_languages + 1):
        percentage = (sum(C) + i) * 100 / N
        rounded_percentage = math.ceil(percentage)
        if rounded_percentage > max_percentage:
            max_percentage = rounded_percentage
    
    return max_percentage

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N, L = map(int, input().split())
        C = list(map(int, input().split()))
        result = max_rounded_percentage(N, L, C)
        results.append(f"Case #{_ + 1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()