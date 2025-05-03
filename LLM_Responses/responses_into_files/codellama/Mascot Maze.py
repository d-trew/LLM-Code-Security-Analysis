import sys
input = sys.stdin.readline
# t = int(input())
t = 1
for case in range(1, t+1):
    n = int(input())
    left_exits = []
    right_exits = []
    for i in range(n):
        left_exit = int(input()) - 1
        right_exit = int(input()) - 1
        left_exits.append(left_exit)
        right_exits.append(right_exit)
    # Check if it's possible to assign mascots while obeying the rules explained above
    if is_possible(n, left_exits, right_exits):
        print("Case #{}: Possible".format(case))
    else:
        print("Case #{}: Impossible".format(case))

def is_possible(n, left_exits, right_exits):
    # Initialize a dictionary to keep track of the mascots for each room
    mascots = {}
    for i in range(n):
        mascots[i] = []
    
    # Assign mascots to rooms based on the left and right exits
    for i in range(n):
        if len(mascots[left_exits[i]]) == 0:
            mascots[i].append("A")
        elif len(mascots[right_exits[i]]) == 0:
            mascots[i].append("B")
    
    # Check if any three consecutive rooms have three different mascots
    for i in range(n-2):
        if mascots[i] != mascots[i+1] and mascots[i+1] != mascots[i+2]:
            return False
    
    # If we reach this point, it means that any three consecutive rooms have three different mascots, so the assignment is possible
    return True