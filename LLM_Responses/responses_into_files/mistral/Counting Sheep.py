from itertools import count, chain, cycle, islice

def bleatrix(n):
    digits = set()
    multiples = chain([n], (i * n for i in count(1)))
    for multiple in multiples:
        if all(d in str(multiple) for d in range(10)):
            return multiple
        else:
            digits.update(str(multiple))
    return "INSOMNIA"

def main():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        print(f"Case #{case}: {bleatrix(n)}")

if __name__ == "__main__":
    main()


This code reads the number of test cases, then for each test case, it runs the `bleatrix` function to find the last number that Bleatrix will name before falling asleep. The `bleatrix` function generates a sequence of multiples of the given number and checks whether all ten digits have appeared in any of these multiples. If so, it returns the multiple; otherwise, it returns "INSOMNIA".