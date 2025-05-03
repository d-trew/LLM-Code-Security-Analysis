import sys

def read_int() -> int:
    return int(sys.stdin.readline())

def read_ints() -> list[int]:
    return [int(x) for x in sys.stdin.readline().split()]

if __name__ == '__main__':
    t = read_int()
    for case in range(1, t + 1):
        n = read_int()
        if n == 0:
            print(f'Case #{case}: INSOMNIA')
        else:
            print(f'Case #{case}: {n}')