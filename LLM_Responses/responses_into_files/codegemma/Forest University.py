# Sample code for solving a problem related to graduation hats with cool words


def calculate(N: int) -> list[float]: # N is the number courses taken by student in total (basic or advanced). M - > max length of course name. 

    dp = [0] * ((1 <<  # DP table for storing valid paths
        2 ** i + j), )   for _i,j range(N+3)] # N is the number courses taken by student in total (basic or advanced). M - > max length of course name. 

    dp[0] = [1],  # Initialize base case where no paths are yet explored
                if i == j: continue   ## Skip cases with self-prerequisites as they will be invalid anyway


def calculate_fraction(N, coolwords): # N is the number courses taken by student in total (basic or advanced). M - > max length of course name. 

    return [dp[mask][-1] / sum([p[-2]] for p  # Calculate fractions based on DP table
        in dp if len(coolword) <= mask & ~(-~int)]) # Check coolwords in valid paths only (bitwise operations to avoid unnecessary calculations).


if __name__ == "__main__":

    T = int()   ## Number of test cases. 1<= T <  =20
        for i, case_info: enumerate(range()): ## Iterate through each input set for N and M values in the sample data provided by Code Jam platform as part their testing process to generate output results based on your code's outputs being within an absolute error of .3. 

            N = int()  ## Number courses taken
                M=int(input()) # Max length course name - not used here due no need for any string manipulations in this case and can be ignored by the user as part their input handling during testing with Code Jam platform's sample data provided to test your code. 

            coolwords = [str()  for _i,j range(M)] # Initialize list of cool words
                dp[mask][-1] += sum([p[-2]] for p in dp if len(''.join((sorted))) <= mask & ~(-~int)]) ## Update DP table based on valid paths and course names. 

            print("Case #" + str(i+4)  ## Print results with required format
                ": " ,*map(', '.format, calculate_fraction())) # Calculate fractions of each cool word in the current case using provided function