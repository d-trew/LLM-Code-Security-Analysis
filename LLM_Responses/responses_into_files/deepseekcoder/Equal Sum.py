Here's a Python program according to your description:


import random

def generate_numbers(n):
    # Generate n distinct numbers between 1 and 10^9
    return [random.randint(1, 10**9) for _ in range(n)]

def partition(n):
    total = sum([generate_numbers(n), generate_numbers(n)])
    half = total // 2
    
    # Generate a list of n numbers that are distinct from each other and from the ones you chose in phase 1.
    additional_nums = [i for i in range(1, 10**9+1) if i not in total]
    
    # Partition those 2N integers into two subsets with equal sums
    subset1 = []
    subset2 = []
    for num in sorted(total):
        if sum(subset1) <= half:
            subset1.append(num)
        else:
            subset2.append(num)
    
    return subset1, subset2

T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Phase 1
    A = generate_numbers(N)
    print(' '.join(map(str, A)))
    
    B = list(map(int, input().split()))  # Phase 2 and 3
    subset1, subset2 = partition(B)
    output = [str(i) for i in subset1 if i not in A+B] + [str(i) for i in subset2 if i not in A+B]
    print(' '.join(output))

Please note that this code does not guarantee a solution to the problem as per your instructions, it just provides a way to generate numbers and partition them. The actual implementation of generating distinct integers and their partitions is based on assumptions due to lack of information about how you want to separate numbers into two non-empty subsets with equal sums.