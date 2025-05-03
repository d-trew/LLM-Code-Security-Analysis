def min_turns_to_defeat_knight(Hd, Ad, Hk, Ak, B, D):
    if Hd <= Ak:
        return "IMPOSSIBLE"
    
    turns = 0
    while True:
        # Your turn
        turns += 1
        Hk -= Ad
        if Hk <= 0:
            return str(turns)
        
        # Knight's turn
        turns += 1
        Hd -= Ak
        if Hd <= 0:
            return "IMPOSSIBLE"

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
T = int(data[0])
results = []
index = 1
for _ in range(T):
    Hd = int(data[index])
    index += 1
    Ad = int(data[index])
    index += 1
    Hk = int(data[index])
    index += 1
    Ak = int(data[index])
    index += 1
    B = int(data[index])
    index += 1
    D = int(data[index])
    index += 1
    
    result = min_turns_to_defeat_knight(Hd, Ad, Hk, Ak, B, D)
    results.append(result)

# Output results
for i, result in enumerate(results):
    print(f"Case #{i + 1}: {result}")