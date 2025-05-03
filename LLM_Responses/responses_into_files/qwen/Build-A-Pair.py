from itertools import permutations

def min_abs_difference(digits):
    digits = list(map(int, digits))
    n = len(digits)
    
    def is_valid(num):
        return num > 0 and '0' not in str(num)
    
    min_diff = float('inf')
    
    for perm in permutations(digits):
        first_num = int(''.join(map(str, perm[:n//2])))
        second_num = int(''.join(map(str, perm[n//2:])))
        
        if is_valid(first_num) and is_valid(second_num):
            diff = abs(first_num - second_num)
            min_diff = min(min_diff, diff)
    
    return min_diff

def solve():
    T = int(input())
    results = []
    
    for i in range(1, T + 1):
        digits = input().strip()
        result = min_abs_difference(digits)
        results.append(f"Case #{i}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()