import sys
from random import shuffle

def generate_network(N):
    computers = list(range(1, N + 1))
    shuffle(computers)
    network = []
    for i in range(N - 1):
        network.append((computers[i], computers[i + 1]))
    return network

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        L = int(data[index])
        U = int(data[index + 1])
        N = (L + U) // 2
        index += 2
        
        network = generate_network(N)
        
        print(N, file=sys.stdout, flush=True)
        for A, B in network:
            print(A, B, file=sys.stdout, flush=True)
        
        X = list(map(int, input().split()))
        results.append(X)
    
    for X in results:
        print(' '.join(map(str, X)), file=sys.stdout, flush=True)

if __name__ == "__main__":
    main()