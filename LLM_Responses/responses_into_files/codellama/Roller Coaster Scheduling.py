import sys

def solve(N, C, M):
    # Create a dictionary to store the tickets and their corresponding customers
    tickets = {}
    for i in range(M):
        pi, bi = map(int, input().split())
        if pi not in tickets:
            tickets[pi] = []
        tickets[pi].append(bi)
    
    # Create a dictionary to store the customers and their corresponding seats
    customers = {}
    for ticket in tickets:
        for customer in tickets[ticket]:
            if customer not in customers:
                customers[customer] = []
            customers[customer].append(ticket)
    
    # Initialize variables to keep track of the minimum number of rides and promotions
    min_rides = sys.maxsize
    min_promotions = sys.maxsize
    
    # Iterate through all possible combinations of seats and customers
    for seat in range(1, N+1):
        for customer in range(1, C+1):
            if seat in customers and customer in customers[seat]:
                promotions = 0
                rides = 1
                # Check if the promotion is possible
                while True:
                    if seat-1 in tickets and customers[seat-1] == [customer]:
                        promotions += 1
                        break
                    elif seat+1 in tickets and customers[seat+1] == [customer]:
                        promotions += 1
                        break
                    else:
                        rides += 1
                        seat = (seat+2) % N
                # Update the minimum number of rides and promotions if necessary
                if rides < min_rides or (rides == min_rides and promotions < min_promotions):
                    min_rides = rides
                    min_promotions = promotions
    
    # Output the minimum number of rides and promotions
    print(f"Case #{x}: {min_rides} {min_promotions}")

T = int(input())
for x in range(1, T+1):
    N, C, M = map(int, input().split())
    solve(N, C, M)