def solve():
    T = int(input())
    for t in range(T):
        D, N = map(int, input().split())
        horses = [list(map(int, input().split())) for _ in range(N)]
        
        # Sort the horses by their initial position (from west to east)
        horses.sort()
        
        # Initialize the maximum speed as D (destination), which is the slowest possible speed
        max_speed = D
        
        # Iterate over the horses in reverse order of their speeds
        for horse in reversed(horses):
            if horse[1] < max_speed:  # If this horse's speed is less than the current maximum speed
                max_speed = (D - horse[0]) / (max_speed - horse[1])  # Calculate the new maximum speed
        
        print(f"Case #{t+1}: {max_speed}")

solve()