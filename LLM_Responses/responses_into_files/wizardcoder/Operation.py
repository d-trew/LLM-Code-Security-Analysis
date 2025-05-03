def main():
    T = int(input())
    for i in range(T):
        S, C = map(int, input().split())
        cards = []
        for _ in range(C):
            op, val = map(str, input().split())
            cards.append((op, int(val)))
        max_value = 0
        min_value = float('inf')
        for perm in itertools.permutations(cards):
            result = S
            for op, val in perm:
                if op == '+':
                    result += val
                elif op == '-':
                    result -= val
                elif op == '*':
                    result *= val
                else:
                    result /= val
            max_value = max(max_value, result)
            min_value = min(min_value, result)
        numerator = int(math.gcd(int(max_value), int(min_value)))
        denominator = 1
        print('Case #{}: {}/{}'.format(i+1, numerator, denominator))
                
if __name__ == '__main__':
    main()