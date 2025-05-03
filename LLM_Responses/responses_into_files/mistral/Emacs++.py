import sys
from collections import defaultdict
input = sys.stdin.readline

def parse_input():
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        program = input()
        moves = list(map(list, zip(*[input().split() for _ in range(3)])))
        queries = list(map(list, zip(*[input().split() for _ in range(2)])))
        yield k, q, program, moves, queries

def move_cost(program, pos1, pos2):
    depth = defaultdict(int)
    total = 0
    i = 0
    while i < len(program):
        if program[i] == '(':
            depth[i] += 1
            total += depth[i]
        elif program[i] == ')':
            depth[i] -= 1
            total += depth[i] + 1
        i += 1
    cost = abs(depth[pos1 - 1]) + abs(depth[pos2 - 1])
    return min(cost, len(program) - cost)

def solve(k, q, program, moves, queries):
    total = 0
    for i, (s, e) in enumerate(queries):
        cost = sum([move_cost(program, s, x) + move_cost(program, x, e) for x in moves[i] if x != (s - 1) and x != (e - 1)])
        total += cost
    return total

for k, q, program, moves, queries in parse_input():
    print(f"Case #{k}: {solve(k, q, program, moves, queries)}")


This code reads the input from standard input, parses it into a format that can be used for computation and solves the problem by iterating through each query and calculating the cost of moving the cursor using the `move_cost` function. The final answer is printed for each case.