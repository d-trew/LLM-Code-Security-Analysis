def min_rides(N, M, tickets):
    # Initialize variables
    seats = [0]*N
    promotions = 0
    rides = 0
    
    # Process each ticket
    for pos, buyer in tickets:
        # If the seat is empty or occupied by another customer, promote it
        while seats[pos-1] != 0 and seats[pos-1] != buyer:
            promotions += 1
            pos -= 1
        
        # Assign the ticket to the seat if it's not already taken
        if seats[pos-1] == 0 or seats[pos-1] == buyer:
            seats[pos-1] = buyer
    
    # Count the number of rides
    for i in range(N):
        if seats[i]:
            rides += 1
            
    return rides, promotions

T = int(input())  # Number of test cases
for tc in range(1, T+1):
    N, C, M = map(int, input().split())  # Seat count, customer count, ticket count
    tickets = [tuple(map(int, input().split())) for _ in range(M)]  # Ticket details (position, buyer)
    
    rides, promotions = min_rides(N, M, tickets)
    
    print("Case #{}: {} {}".format(tc, rides, promotions))