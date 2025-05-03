def longest_straight(dice):
    sides = [0] * (max(dice) + 1)
    for die in dice:
        sides[die] += 1

    max_length = 0
    current_length = 0
    for side in range(1, len(sides)):
        if sides[side] > 0:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
    return max(max_length, current_length)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        dice = list(map(int, data[index + 1:index + N + 1]))
        index += N + 1
        result = longest_straight(dice)
        results.append(f"Case #{_ + 1}: {result}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()