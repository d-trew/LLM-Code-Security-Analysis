import sys

# Read the input
T, A, B = map(int, sys.stdin.readline().split())

# Process each test case
for i in range(1, T+1):
    # Read the radius and center of the dartboard
    R, X, Y = map(int, sys.stdin.readline().split())
    
    # Initialize variables for the current test case
    num_exchanges = 0
    last_response = ""
    
    # Process up to 300 exchanges with the judge
    while True:
        # Get the next input from Mika
        x, y = map(int, sys.stdin.readline().split())
        
        # Calculate the distance between Mika's throw and the center of the dartboard
        dist = ((x-X)**2 + (y-Y)**2)**0.5
        
        # Check if Mika hit the center of the dartboard or not
        if dist <= R:
            last_response = "CENTER"
            break
        else:
            last_response = "WRONG"
            
        # Update the number of exchanges made so far
        num_exchanges += 1
        
        # Print the response from Gary
        print(last_response)
        
        # Check if Mika has thrown more than 300 darts or if she has received a wrong answer
        if num_exchanges == 300 or last_response == "WRONG":
            break
    
    # If Mika hit the center of the dartboard in all 300 exchanges, print CENTER
    if last_response == "CENTER":
        print("CENTER")
        
    # Otherwise, print WRONG
    else:
        print("WRONG")