def longest_straight(dice):
    numbers = set()
    for die in dice:
        numbers.update(die)
    longest = 0
    while len(numbers) > 0:
        start = min(numbers)
        current = start
        count = 1
        numbers.remove(start)
        while current + 1 in numbers:
            current += 1
            count += 1
            numbers.remove(current)
        longest = max(longest, count)
    return longest

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        N = int(data[index])
        index += 1
        dice = [list(map(int, data[index:index+6])) for _ in range(N)]
        index += 6 * N
        result = longest_straight(dice)
        results.append(result)
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    solve()