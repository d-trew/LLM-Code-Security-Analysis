import sys

def solve(n_kids, bffs):
    # Initialize a dictionary to keep track of the kids and their BFFs
    kid_bffs = {}
    for i in range(len(bffs)):
        kid_bffs[i+1] = bffs[i]
    
    # Initialize a list to store the BFF pairs
    bff_pairs = []
    
    # Iterate through each kid and their BFF
    for i in range(1, n_kids + 1):
        bff = kid_bffs[i]
        
        # If the BFF is not in the list of BFF pairs, add it
        if bff not in bff_pairs:
            bff_pairs.append(bff)
        
        # If the BFF is already in the list of BFF pairs, remove it
        elif bff in bff_pairs:
            bff_pairs.remove(bff)
    
    # Return the length of the list of BFF pairs, which is the maximum number of kids that can be in a circle with their BFFs
    return len(bff_pairs)

def main():
    t = int(input())
    for i in range(t):
        n_kids = int(input())
        bffs = list(map(int, input().split()))
        print("Case #" + str(i+1) + ": " + str(solve(n_kids, bffs)))

if __name__ == '__main__':
    main()