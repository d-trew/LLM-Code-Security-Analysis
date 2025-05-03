import sys
from random import randint, uniform

def main():
    # Read T (number of test cases)
    T = int(input())
    
    for i in range(T):
        # Read N (number of lollipops)
        N = int(input())
        
        # Initialize sold flavors to an empty list
        sold_flavors = []
        
        # Read customer preferences and sell them a lollipop
        for j in range(N):
            # Read D (number of liked flavors)
            D = int(input())
            
            # Read the liked flavor IDs
            liked_flavors = list(map(int, input().split()))
            
            # Find available flavors and choose one randomly
            available_flavors = [f for f in range(N) if f not in sold_flavors]
            if len(available_flavors) == 0:
                print(-1, flush=True)
            else:
                # Choose a random flavor from the available ones
                chosen_flavor = randint(0, len(available_flavors)-1)
                
                # Sell it to the customer and mark as sold
                print(available_flavors[chosen_flavor], flush=True)
                sold_flavors.append(available_flavors[chosen_flavor])
        
        # Check if you sold enough lollipops
        if len(sold_flavors) < 0.9*N:
            print("Too few lollipops sold", file=sys.stderr)
            sys.exit()
    
if __name__ == "__main__":
    main()