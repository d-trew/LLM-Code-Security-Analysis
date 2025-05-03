import collections

def max_customers(pancakes):
    deque = collections.deque(pancakes)
    total = 0
    while len(deque) > 1:
        if deque[0] >= min(deque[-1], deque[1]):
            deque.popleft()
        else:
            deque.pop()
        total += 1
    return total + 1

def main():
    num_cases = int(input())
    for i in range(num_cases):
        n = int(input())
        pancakes = list(map(int, input().split()))
        print("Case #{}: {}".format(i+1, max_customers(pancakes))

if __name__ == "__main__":
    main()