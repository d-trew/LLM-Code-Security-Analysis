import sys

def find_broken_workers(N, B, F):
    # Initialize a list to store the result of TEST_STORE calls
    results = []
    
    # Make up to F calls to TEST_STORE
    for _ in range(min(F, N)):
        test_input = ''.join('1' if i % 2 == 0 else '0' for i in range(N))
        sys.stdout.write(test_input + '\n')
        sys.stdout.flush()
        result = sys.stdin.readline().strip()
        results.append(result)
    
    # Analyze the results to identify broken workers
    broken_workers = []
    for i in range(N):
        if all(result[i] == '1' for result in results):
            broken_workers.append(i)
    
    # Ensure we have exactly B broken workers
    while len(broken_workers) > B:
        broken_workers.pop()
    while len(broken_workers) < B:
        broken_workers.append(-1)
    
    # Sort the broken workers and return them
    broken_workers.sort()
    return broken_workers

# Read input from stdin
T = int(input())
results = []

for _ in range(T):
    N, B, F = map(int, input().split())
    broken_workers = find_broken_workers(N, B, F)
    sys.stdout.write(' '.join(map(str, broken_workers)) + '\n')
    sys.stdout.flush()