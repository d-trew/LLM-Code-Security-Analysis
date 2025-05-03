import sys
sys.setrecursionlimit(10**6) # Increase recursion limit for large inputs
from collections import defaultdict, deque

def read_input():
    T = int(input())
    cases = []
    for i in range(T):
        J, C, A, Q = map(int, input().split())
        adjacency_list = defaultdict(set)
        for _ in range(C):
            U, V = map(int, input().split())
            adjacency_list[U].add(V)
            adjacency_list[V].add(U)
        cases.append((J, C, A, Q, adjacency_list))
    return T, cases

def find_shortest_path(adjacency_list, start, end):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        current_junction, distance = queue.popleft()
        if current_junction == end:
            return distance
        for neighbor in adjacency_list[current_junction]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1 # No path found

def queen_moves(adjacency_list, current_pos, herald):
    next_move = herald[current_pos]
    if next_move == current_pos:
        return False # Alice caught
    del herald[current_pos]
    for neighbor in adjacency_list[next_move]:
        if neighbor not in herald:
            herald[neighbor] = next_move
    return True

def alice_moves(adjacency_list, current_pos):
    distances = [find_shortest_path(adjacency_list, current_pos, target) for target in adjacency_list[current_pos]]
    if not any(distances): # No possible move
        return False # Caught by the Queen
    return min(distances.index(min(distances)) + 1 # Minimum distance to a junction with no herald

def main():
    T, cases = read_input()
    for i in range(T):
        J, C, A, Q, adjacency_list = cases[i]
        herald = {Q: -1} # Initial position of the Queen's herald
        alice_move = 0
        queen_move = 0
        while True:
            if not queen_moves(adjacency_list, Q, herald): # Queen caught Alice
                print("Case #{}: {}".format(i+1, alice_move + queen_move))
                break
            if not alice_moves(adjacency_list, A): # Alice caught by the Queen
                print("Case #{}: {}".format(i+1, "SAFE")
                break
            alice_move += 1
            queen_move += 1
            if alice_move + queen_move >= 2*10**9: # Both have made half the moves each
                print("Case #{}: {}".format(i+1, "SAFE")
                break
        else: # Alice not caught after 10^9 moves
            print("Case #{}: {}".format(i+1, alice_move + queen_move)
            
if __name__ == "__main__":
    main()