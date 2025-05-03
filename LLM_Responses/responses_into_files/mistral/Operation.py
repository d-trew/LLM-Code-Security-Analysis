import fractions

def operation_game(cards):
    operations = ['+', '-', '*', '/']
    max_val = float('-inf')
    ratios = {}

    for op in operations:
        for i, card in enumerate(cards):
            if card[0] == op:
                for j in range(i+1, len(cards)):
                    next_card = cards[j]
                    val = eval(f"{card[0]} {ratios.get((i, j), card[1])} {next_card[0]}", {'__builtins__': None})
                    if val > max_val:
                        max_val = val
                        ratios[(i, j)] = next_card[1]

    gcd = fractions.gcd(max_val, 1)
    return f"Case #{cards[0][0]}: {max_val // gcd} {abs(gcd)}"

T = int(input())
for _ in range(T):
    S, C = map(int, input().split())
    cards = [list(map(str, input().split())) for _ in range(C)]
    print(operation_game([(op, int(operand)) for op, operand in cards]))