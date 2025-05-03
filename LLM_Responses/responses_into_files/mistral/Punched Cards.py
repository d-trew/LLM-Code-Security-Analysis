import sys

def print_punched_card(r, c):
    if r <= 0 or c <= 0:
        return

    lines = (2 * r + 1) * ['-']
    lines[0] = '.' + '.'*(c - 1) + '-'
    for i in range(r):
        lines[i*2 + 1] = '|.|' + ('.'*(c-2)) + '|'
    lines[-1] = '-' + '+' * c + '-'
    for i, line in enumerate(lines[1:-1]):
        print(''.join([lines[i][j] if j != 0 and j != len(line) - 1 else '+' if (i == r//2 and j == c//2) else '.' for j in range(len(line))]))
    print()

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        r, c = map(int, sys.stdin.readline().strip().split(' '))
        print(f"Case #{_ + 1}:")
        print_punched_card(r, c)