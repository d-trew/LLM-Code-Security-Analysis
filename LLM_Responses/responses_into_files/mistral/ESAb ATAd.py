import sys
from collections import deque
import random

def query(pos):
    # Send a query for the bit at position pos
    print(f"Q {pos}")
    sys.stdout.flush()
    return int(input())

def exchange():
    # Get the array from the judge
    print("N")
    sys.stdout.flush()
    arr = list(map(int, input().split()))
    return arr

def quantum_fluctuation(pos):
    # Simulate a quantum fluctuation on the given position
    effects = [0] * pos + [1] + [0] *(len(arr) - pos)
    random.shuffle(effects)
    return effects[pos]

T, B = map(int, input().split())
for _ in range(T):
    arr = exchange()
    q_queries = deque()
    for _ in range(150):
        pos = int(input())
        q_queries.append((pos, query(pos)))
    # Simulate quantum fluctuations on the queries
    flips = [quantum_fluctuation(q[0]) for q in q_queries]
    # Construct the actual array from the flipped and unflipped positions
    arr = [sum([arr[i - 1] if f else 1 - arr[i - 1] for i, f in enumerate(flips)]) for _ in range(B)]
    print("A", ' '.join(map(str, arr)))


This code reads the number of test cases and the length of the array, then processes each test case by exchanging the array with the judge. It allows making up to 150 queries and simulates quantum fluctuations on those queries. The final array is constructed based on the flipped and unflipped positions.