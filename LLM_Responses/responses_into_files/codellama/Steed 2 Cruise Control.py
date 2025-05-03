import math

def f(D, N, Kis, Sis):
    # Find the maximum constant speed (in km/h) that Annie can use without colliding with other horses.
    
    # Initialize variables
    max_speed = 0
    destination = D
    num_other_horses = N
    initial_positions = Kis
    speeds = Sis
    
    # Calculate the maximum speed that Annie can choose without colliding with other horses
    for i in range(num_other_horses):
        distance = abs(initial_positions[i] - destination)
        travel_time = distance / speeds[i]
        if travel_time > max_speed:
            max_speed = travel_time
    
    return math.ceil(max_speed * 10 ** 6) / 10 ** 6 # round to 6 decimal places

def main():
    # Get the number of test cases
    T = int(input())
    
    for t in range(T):
        # Get the destination position and the number of other horses on the road
        D, N = map(int, input().split())
        
        # Get the initial positions and maximum speeds of the other horses
        Kis = [0] * N
        Sis = [0] * N
        for i in range(N):
            Kis[i], Sis[i] = map(int, input().split())
        
        # Find the maximum constant speed (in km/h) that Annie can use without colliding with other horses
        max_speed = f(D, N, Kis, Sis)
        
        # Print the result
        print("Case #" + str(t+1) + ": " + str(max_speed))
    
if __name__ == "__main__":
    main()