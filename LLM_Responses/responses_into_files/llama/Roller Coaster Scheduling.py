import sys

def min_rides_and_promotions(n, m, buyers):
    buyers.sort()
    last_seat = [0] * (n + 1)
    for i in range(m):
        buyer = buyers[i]
        seat = buyers.index(buyer) + 1
        if seat > last_seat[seat]:
            return "Case #{}: {} {}".format(sys._getframe().f_lineno, m, m - len([i for i in buyers if buyers.index(i) >= seat]))
    seats_used = sum([i > j for i, j in zip(buyers, buyers[1:])])
    rides = (seats_used + 1) // n
    promotions = seats_used % n
    return "Case #{}: {} {}".format(1, rides, promotions)

T = int(input())
for _ in range(T):
    n, c, m = map(int, input().split())
    buyers = [int(x) for x in input().split()]
    print(min_rides_and_promotions(n, m, buyers))