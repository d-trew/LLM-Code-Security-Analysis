def print_punched_card(R, C):
    top_border = '-' * (C * 4 - 1)
    middle_row = '|.' + '.' * (C - 2) + '.|'
    bottom_border = '+' + '-' * (C * 2 - 2) + '+'

    print(top_border)
    for _ in range(R):
        print(middle_row)
    print(bottom_border)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1

    results = []
    for t in range(1, T + 1):
        R = int(data[index])
        C = int(data[index + 1])
        index += 2
        result = f"Case #{t}:\n"
        print_punched_card(R, C)
        results.append(result)

    sys.stdout.write('\n'.join(results))

if __name__ == "__main__":
    main()