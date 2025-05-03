import sys

def solve(N, M, S):
    # Initialize a dictionary to store the positions of the attendees
    positions = {}
    for i in range(1, N+1):
        positions[i] = (0, 0)

    # Loop through the duck meetings and update the positions of the attendees
    for i in range(M):
        x, y, t = map(int, input().split())
        positions[x] = (positions[x][0], positions[x][1]+t)
        positions[y] = (positions[y][0], positions[y][1]+t)

    # Loop through the statements and check if they are feasible
    for i in range(S):
        a, b, u, v, d = map(int, input().split())
        if not is_feasible(positions, a, b, u, v, d):
            return "IMPOSSIBLE"

    # Find the minimum number of ducks that might have infiltrated the conference
    min_ducks = 0
    for i in range(1, N+1):
        if positions[i][0] > 0 or positions[i][1] > 0:
            min_ducks += 1

    return min_ducks

def is_feasible(positions, a, b, u, v, d):
    # Check if the statement is feasible by checking if both attendees are at the same point
    # after the specified time
    if positions[a][0] == positions[b][0] and positions[a][1] == positions[b][1]:
        return True
    else:
        return False

# Read the input
T = int(input())
for t in range(T):
    N, M, S = map(int, input().split())
    print("Case #" + str(t+1) + ": " + str(solve(N, M, S)))