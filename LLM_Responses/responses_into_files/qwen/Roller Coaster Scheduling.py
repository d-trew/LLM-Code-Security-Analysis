def min_rides_and_promotions(N, C, M, tickets):
    from collections import defaultdict

    seat_to_customers = defaultdict(list)
    customer_to_seats = defaultdict(list)

    for Pi, Bi in tickets:
        seat_to_customers[Pi].append(Bi)
        customer_to_seats[Bi].append(Pi)

    rides = 0
    promotions = 0

    while seat_to_customers:
        assigned_rides = set()
        for seat in sorted(seat_to_customers.keys()):
            if seat not in assigned_rides:
                ride_customers = []
                for customer in seat_to_customers[seat]:
                    if any(pos in assigned_rides for pos in customer_to_seats[customer]):
                        continue
                    ride_customers.append(customer)
                    assigned_rides.update(customer_to_seats[customer])
                if ride_customers:
                    rides += 1
                    promotions += len(ride_customers) - 1

        remaining_tickets = [(seat, customer) for seat in seat_to_customers.keys() for customer in seat_to_customers[seat]]
        seat_to_customers.clear()
        for Pi, Bi in remaining_tickets:
            if Pi not in assigned_rides:
                seat_to_customers[Pi].append(Bi)

    return rides, promotions

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for t in range(1, T + 1):
        N = int(data[index])
        index += 1
        C = int(data[index])
        index += 1
        M = int(data[index])
        index += 1

        tickets = []
        for _ in range(M):
            Pi = int(data[index])
            index += 1
            Bi = int(data[index])
            index += 1
            tickets.append((Pi, Bi))

        rides, promotions = min_rides_and_promotions(N, C, M, tickets)
        results.append(f"Case #{t}: {rides} {promotions}")

    print('\n'.join(results))

if __name__ == "__main__":
    solve()