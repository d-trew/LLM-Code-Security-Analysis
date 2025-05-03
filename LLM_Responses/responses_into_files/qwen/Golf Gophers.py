import sys
from collections import deque

def read_input():
    return [int(x) for x in input().split()]

def send_output(output):
    print(output)
    sys.stdout.flush()

def simulate_gophers(nights, max_gophers):
    blades = [2] * 18  # Initially all windmills have 2 blades
    gopher_count = 0

    for _ in range(nights):
        for i in range(18):
            if blades[i] == 0:
                gopher_count += 1
                break
            blades[i] -= 1
            if blades[i] < 0:
                blades[i] += 2

    return gopher_count

def main():
    input_data = read_input()
    T, N, M = input_data[0], input_data[1], input_data[2]

    for _ in range(T):
        nights_left = N
        while nights_left > 0:
            send_output(nights_left)
            response = read_input()[0]
            if response == -1:
                break
            nights_left -= 1

if __name__ == "__main__":
    main()