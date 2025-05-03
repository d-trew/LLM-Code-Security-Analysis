def min_training_cost(N, workers):
    max_machines = [0] * N
    for worker in workers:
        machines = [i for i, knows in enumerate(worker) if knows == '1']
        for machine in machines:
            max_machines[machine] = max(max_machines[machine], len(machines))
    
    return sum(max_machines)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        workers = [data[index + i] for i in range(N)]
        index += N
        
        result = min_training_cost(N, workers)
        results.append(f"Case #{_ + 1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()