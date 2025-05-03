import sys

def read_input():
    return [int(x) for x in input().split()]

def write_output(data):
    print(*data, flush=True)

def main():
    T, N, K = read_input()
    for _ in range(T):
        balls = read_input()
        colors = list(range(1, N + 1))
        for _ in range(K):
            write_output(colors)
            result = read_input()
            if result == balls:
                break
            # Update colors based on the current state of the balls
            new_colors = [colors[i] for i in range(N) if result[i] != balls[i]]
            colors = list(range(1, N + 1))
        else:
            print("Failed to sort", file=sys.stderr)

if __name__ == "__main__":
    main()