def min_parentheses(digits):
    n = len(digits)
    stack = []
    result = [''] * n
    
    for i, digit in enumerate(digits):
        depth = int(digit)
        open_needed = depth - (len(stack) - sum(1 for s in stack if s == '('))
        
        while open_needed > 0:
            result[i] += '('
            stack.append('(')
            open_needed -= 1
        
        result[i] += digit
        
        close_needed = len(stack) - (depth * 2)
        while close_needed > 0:
            result[i] += ')'
            stack.pop()
            close_needed -= 1
    
    return ''.join(result)

def solve():
    T = int(input())
    results = []
    
    for i in range(1, T + 1):
        digits = input().strip()
        result = min_parentheses(digits)
        results.append(f"Case #{i}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()