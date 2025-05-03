from fractions import Fraction
from itertools import permutations

def max_value(S, C, cards):
    operations = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}
    
    def evaluate(cards_order):
        result = Fraction(S)
        for op, val in cards_order:
            result = operations[op](result, Fraction(val))
        return result
    
    max_result = Fraction('-inf')
    best_order = None
    for order in permutations(cards):
        current_result = evaluate(order)
        if current_result > max_result:
            max_result = current_result
            best_order = order
    
    return max_result.numerator, max_result.denominator

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        S = int(data[index])
        C = int(data[index + 1])
        cards = [(data[index + 2 + i * 2], int(data[index + 3 + i * 2])) for i in range(C)]
        index += 2 + C * 2
        result = max_value(S, C, cards)
        results.append(f"Case #{_ + 1}: {result[0]} {result[1]}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()