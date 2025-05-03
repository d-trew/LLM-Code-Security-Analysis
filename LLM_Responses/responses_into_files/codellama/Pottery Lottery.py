import sys

# Read number of test cases from input
T = int(input())

for i in range(T):
    # Read current day and vase information from input
    day, vase = map(int, input().split())
    
    # Simulate action of previous player on the same day
    if day > 1:
        prev_vase = int((day - 1) * (day - 2) / 2)
        print("-1", file=sys.stderr)
    
    # Insert token in vase on turn 100
    if day == 100:
        print(100, 100)
        continue
    
    # Print the vase number and probability of winning
    if vase > 20 or vase < 0:
        print("-1", file=sys.stderr)
    else:
        print(vase, 10)