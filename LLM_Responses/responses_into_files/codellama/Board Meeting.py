import sys

# Read input
T = int(input())
Nmax = int(input())
M = int(input())
R = int(input())

for t in range(T):
    # Phase 1: propose meeting location and get number of moves
    A, B = map(int, input().split())
    print(max([abs(A-Xi)+abs(B-Yi) for Xi, Yi in kings]))
    
    # Phase 2: judge tells us the total number of moves
    C, D = map(int, input().split())
    print(sum([max(abs(C-Xi), abs(D-Yi)) for Xi, Yi in kings]))

# Print "READY" to indicate that we are ready for the second phase
print("READY")

# Phase 3: judge sends us the first request of the second phase
C, D = map(int, input().split())

# Process all requests sent by the judge
for i in range(R):
    # Print the total number of moves used by all kings to get to the meeting cell
    print(sum([max(abs(C-Xi), abs(D-Yi)) for Xi, Yi in kings]))

# Once we have processed all requests, print "DONE" to indicate that we are done
print("DONE")