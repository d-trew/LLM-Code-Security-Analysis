def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        workers_machines = []
        for _ in range(N):
            workers_machines.append([int(x) for x in input()])
        
        max_operators = sum(max(row) for row in workers_machines)
        min_dollars = 0
        for i in range(N):
            num_operators = sum(workers_machines[i])
            if num_operators < max_operators:
                min_dollars += (max_operators - num_operators)
        
        print("Case #%d: %d" % (i+1, min_dollars))
    
main()