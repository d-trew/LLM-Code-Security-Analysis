import sys

def solve(n, AC, AJ):
    # Initialize variables
    exchanges = 0
    schedule = []
    
    # Check if the input is valid
    if n < 1 or AC < 0 or AJ < 0:
        return -1
    
    # Add activities to the schedule
    for i in range(AC):
        start, end = map(int, input().split())
        schedule.append((start, end))
    
    for i in range(AJ):
        start, end = map(int, input().split())
        schedule.append((start, end))
    
    # Sort the schedule by start time
    schedule.sort(key=lambda x: x[0])
    
    # Iterate through the schedule and check for exchanges
    for i in range(len(schedule) - 1):
        if schedule[i][1] > schedule[i + 1][0]:
            exchanges += 1
    
    return exchanges

# Read input
n = int(input())
AC = int(input())
AJ = int(input())

# Call the solve function and print the result
result = solve(n, AC, AJ)
print(result)