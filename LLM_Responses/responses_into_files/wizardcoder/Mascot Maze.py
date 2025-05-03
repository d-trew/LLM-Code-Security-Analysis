import sys
from collections import defaultdict

def assign_mascots(N):
    left_exits = list(map(int, input().split()))
    right_exits = list(map(int, input().split()))
    
    # Create a graph to represent the maze
    graph = {i: [left_exits[i], right_exits[i]] for i in range(N)}
    
    # Initialize dictionary of visited rooms and mascots
    visited_rooms = defaultdict(set)
    assigned_mascots = {}
    
    # Start at room 1 and recursively assign mascots to each connected component
    def dfs(room, mascot):
        # If we have already visited this room before, check if the mascot is valid
        if room in visited_rooms[room]:
            return assigned_mascots.get(room) == mascot
        
        # Mark room as visited and assign mascot to it
        visited_rooms[room].add(mascot)
        assigned_mascots[room] = mascot
    
        # Recurse on both exits with the same mascot
        for exit in graph[room]:
            if not dfs(exit, mascot):
                return False
        
        # If we have visited all rooms in this component, return True
        if len(visited_rooms) == N:
            return True
    
    # Try each of the 13 possible mascots and check if they can be assigned to each connected component
    for i, mascot in enumerate("ACDEHIJKMORST"):
        visited_rooms.clear()
        assigned_mascots.clear()
        
        # Start at room 1 with the current mascot
        if dfs(1, mascot):
            return "IMPOSSIBLE" not in [assign_mascots(i+2) for i in range(N)]
    
    # If we reach here without returning, then no valid assignment was found
    return "IMPOSSIBLE"
        
# Read input and process each test case
T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    # Read the maze layout and check if it is possible to assign mascots without breaking rules
    result = assign_mascots(N)
    
    print("Case #{}: {}".format(t, result))