def main():
    T = int(input())
    
    for i in range(1, T+1):
        S = int(input())
        
        D = []
        A = []
        B = []
        
        for j in range(S):
            Di, Ai, Bi = map(int, input().split())
            D.append(Di)
            A.append(Ai)
            B.append(Bi)
            
        # Sort the signs by their distance from Signfield (west to east)
        D_sorted = sorted(D)
        
        # Initialize variables for largest possible number of signs and valid sets
        max_signs = 1
        valid_sets = 0
        
        # Iterate through all possible lengths of subsequence starting from 2 up to the length of the sequence
        for k in range(2, S+1):
            # Initialize variables for current subsequence and its sign count
            curr_subseq = []
            curr_signs = 0
            
            # Iterate through all possible subsequences of signs with length k
            for j in range(S-k+1):
                subseq = D_sorted[j:j+k]
                
                # Check if the current subsequence is valid
                if subseq[-1] - subseq[0] == sum(subseq) and all((subseq[i+1] - subseq[i]) >= A[D.index(subseq[i]) for i in range(k-1)):
                    curr_signs = k
                    
                # Update max_signs if the current subsequence is longer than previous longest valid subsequence found
                if curr_signs > max_signs:
                    max_signs = curr_signs
                    
            # Increment count of valid sets with length equal to max_signs
            if curr_signs == max_signs:
                valid_sets += 1
        
        print(f"Case #{i}: {max_signs} {valid_sets}")

if __name__ == "__main__":
    main()