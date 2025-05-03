import math

def compute_probability(machines, links):
    num_intranets = 0
    for i in range(machines):
        for j in range(i+1, machines):
            if links[(i,j)] == 0:
                continue
            else:
                num_intranets += 1
    return num_intranets / math.factorial(machines)

T = int(input())
for t in range(T):
    machines, K = map(int, input().split())
    links = {}
    for i in range(machines):
        for j in range(i+1, machines):
            links[(i,j)] = 0
    for k in range(K):
        link = list(map(int, input().split()))
        links[link] += 1
    print("Case #" + str(t+1) + ": " + str(compute_probability(machines, links)))