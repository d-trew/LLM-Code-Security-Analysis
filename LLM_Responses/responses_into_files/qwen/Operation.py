import fractions
def solve_case(cards):
    start = int(input())
    operations = []
    for _ in range(int(input())):
        operation, operand = input().split()
        operations.append((operation == '+', int(operand)))
    max_result = float('-inf')
    for order in range(len(list(map(lambda x: 1 if x[0] == '-' else -1, operations)))):
        result = start
        for op, operand in operations:
            if op:
                result += operand
            else:
                result /= operand
        max_result = max(max_result, result)
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    z = 1
    for op, operand in operations:
        if op:
            z = abs(z * operand)
        else:
            z = abs(z * operand)
    y = int(max_result * z)
    z = int(gcd(z, y))
    return f"Case #{int(input()) + 1}: {y//z} {z}"