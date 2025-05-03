Here is the Python code for the problem:


import sys
from collections import defaultdict

def solve(n, machines):
    workers = [defaultdict(set) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if machines[i][j] == '1':
                workers[j][i].add('m')
    
    lessons = 0
    for worker in workers:
        known = set()
        to_learn = n - len(worker)
        while to_learn > 0:
            machines_to_learn, _ = max((len(v), k) for (k, v) in worker.items())
            lessons += min(machines_to_learn, to_learn) * 2
            known |= set(worker[max((len(v), k) for (k, v) in worker.items())[1]])
            to_learn -= min(machines_to_learn, to_learn)
            
            if len(known) == n:
                break
                
            for w in known:
                del worker[w]
    return lessons

def main():
    t = int(input().strip())
    for i in range(1, t + 1):
        n = int(input().strip())
        machines = [input().strip() for _ in range(n)]
        print("Case #{}: {}".format(i, solve(n, machines)))

if __name__ == "__main__":
    main()

This code uses a greedy algorithm to find the minimum number of lessons required. It maintains a dictionary for each worker where keys are machine numbers and values are sets of workers who know how to operate that machine. For each worker, it finds out which machines they can still learn without knowing all machines (this is done by comparing their current knowledge with the total number of machines). The maximum number of machines a worker can learn in one lesson is chosen for every worker. If there are more lessons required than workers know how to operate, then the remaining workers will have to be taught less and hence the cost increases.