# This is a Python program to simulate the broken worker database system described above. It reads input from stdin and writes output to stdout.

import sys

def main():
    T = int(input()) # read number of test cases
    
    for i in range(T):
        N, B, F = map(int, input().split())  # read the number of workers and broken workers
        
        bits = []
        calls = 0
        broken_workers = [False] * N
        
        while len(bits) < N:
            if calls >= F:
                print("-1")
                sys.exit()
            
            line = input().strip()
            bits += [int(c) for c in line]
            calls += 1
        
        for j in range(N):
            if not broken_workers[j]:
                print(bits[j], end=' ')
        
        print("") # newline after each test case output
        
if __name__ == "__main__":
    main()