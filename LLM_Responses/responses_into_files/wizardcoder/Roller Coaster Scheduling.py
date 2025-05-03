def main():
    T = int(input())
    for i in range(T):
        N, C, M = map(int, input().split())
        seats = [[] for _ in range(N+1)]
        for j in range(M):
            P, B = map(int, input().split())
            seats[P].append(B)
        
        rides = 0
        promotions = 0
        
        while any([len(seat) > 1 for seat in seats]):
            rides += 1
            
            # Find the first seat with multiple buyers
            max_buyers = []
            for j in range(N, 0, -1):
                if len(seats[j]) > 1:
                    max_buyers.append(j)
                    break
            
            # Promote the first buyer to a lower seat
            seats[max_buyers[-1]].pop(0)
            promotions += 1
            
            for k in range(len(seats[max_buyers[-2])):
                if len(seats[k]) == 0 or seats[k][-1] != max_buyers[-1]:
                    seats[k].append(max_buyers[-1])
                    
            # Remove the first buyer from the second highest seat
            seats[j].pop(0)
        
        rides += len([seat for seat in seats if len(seat) > 0])
        print("Case #{}: {} {}".format(i+1, rides, promotions))
            
if __name__ == "__main__":
    main()