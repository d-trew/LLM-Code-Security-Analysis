import sys

def solve(C):
    # Initialize a dictionary to store the hiking tours and their durations
    tours = {}
    for i in range(1, C + 1):
        tours[i] = []

    # Read the input data
    for i in range(2 * C):
        Ei, Li, Di = map(int, sys.stdin.readline().split())
        tours[Ei].append((Li, Di))

    # Initialize a dictionary to store the camps and their hiking tours
    camps = {}
    for i in range(1, C + 1):
        camps[i] = []

    # Find the start and end times of each tour
    for i in range(1, C + 1):
        for j in range(2):
            Li, Di = tours[i][j]
            if j == 0:
                # Start time
                camps[i].append((Li, "start"))
            else:
                # End time
                camps[i].append((Li + Di, "end"))

    # Initialize the current camp and time
    current_camp = 1
    current_time = 0

    # Iterate through each tour
    for i in range(1, C + 1):
        # Get the start and end times of the tour
        start_time, _ = camps[i][0]
        _, end_time = camps[i][-1]

        # Calculate the duration of the tour
        duration = end_time - start_time

        # Check if the current time is between the start and end times of the tour
        if current_time >= start_time and current_time <= end_time:
            # If it is, add the duration to the total time
            current_time += duration
        else:
            # If it's not, skip this tour
            continue

    return current_time

if __name__ == "__main__":
    C = int(input())
    print("Case #1:", solve(C))