import sys

def main():
    T = int(input())
    for _ in range(T):
        while True:
            V = ''.join(format(i, '08b') for i in range(8))
            print(V)
            sys.stdout.flush()
            N = int(input())
            if N == 0:
                break

if __name__ == "__main__":
    main()