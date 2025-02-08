def solve():
    N, C, M = map(int, input().split())
    tickets = []
    for _ in range(M):
        P, B = map(int, input().split())
        tickets.append((P, B))

    customer_tickets = {}
    for P, B in tickets:
        customer_tickets[B] = customer_tickets.get(B, []) + [(P)]

    min_rides = float('inf')
    min_promotions = float('inf')

    for i in range(1 << M):
        promotions = 0
        current_tickets = []
        for j in range(M):
            P, B = tickets[j]
            if (i >> j) & 1:
                promotions += 1
                new_P = min(P -1,1)
                current_tickets.append((new_P,B))

            else:
                current_tickets.append((P,B))

        
        rides_needed = 0
        seated = {}
        
        while True:
            rides_needed +=1
            current_ride = {}
            available_seats = list(range(1,N+1))
            
            sorted_tickets = sorted(current_tickets, key=lambda x: x[0])
            
            
            possible = True
            for pos,cust in sorted_tickets:
                if cust not in seated:
                    if pos in available_seats:
                        
                        idx = available_seats.index(pos)
                        available_seats.pop(idx)
                        seated[cust] = seated.get(cust,[])+[rides_needed]
                        

            
            unseated = [item for item in current_tickets if item[1] not in seated or len(seated[item[1]])<len([x for x in current_tickets if x[1]==item[1]])]
            
            if len(unseated)==0:
                break

        if rides_needed < min_rides:
            min_rides = rides_needed
            min_promotions = promotions
        elif rides_needed == min_rides:
            min_promotions = min(min_promotions, promotions)
    return min_rides, min_promotions


T = int(input())
for i in range(1, T + 1):
    result_rides, result_promotions = solve()
    print(f"Case #{i}: {result_rides} {result_promotions}")