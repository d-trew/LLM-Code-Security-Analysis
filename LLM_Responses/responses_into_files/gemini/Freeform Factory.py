def solve():
    N = int(input())
    abilities = []
    for _ in range(N):
        abilities.append(input())

    def check(assignment):
        for i in range(N):
            worker_abilities = []
            for j in range(N):
                if abilities[i][j] == '1' or assignment[i][j] == 1:
                    worker_abilities.append(j)

            if not worker_abilities:
                return False

        
        for perm in permutations(range(N)):
            assigned_machines = [-1] * N
            
            for worker_index in perm:
                available_machines = []
                for machine_index in range(N):
                    if (abilities[worker_index][machine_index] == '1' or assignment[worker_index][machine_index] == 1) and assigned_machines[machine_index] == -1:
                        available_machines.append(machine_index)
                
                if available_machines:
                    chosen_machine = available_machines[0] #Simulate random choice - always pick the first available.
                    assigned_machines[chosen_machine] = worker_index
            
            if -1 in assigned_machines:
                return False
        return True

    from itertools import permutations
    
    min_cost = float('inf')
    for i in range(2**(N*N)):
        assignment = [[0 for _ in range(N)] for _ in range(N)]
        cost = 0
        temp = bin(i)[2:].zfill(N*N)
        k=0
        for r in range(N):
            for c in range(N):
                if temp[k] == '1':
                    assignment[r][c] = 1
                    cost +=1
                k+=1

        if check(assignment):
            min_cost = min(min_cost, cost)

    return min_cost


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")