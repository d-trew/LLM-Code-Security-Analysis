3    


def countDivisible(S , D):        # Function that counts the number of divisible divisions     for a given string S and divisor d  in base ten   within range [1, len (str) -2] we have to check if consecutive substrings are not divisble by 7. If so then it is only possible for all numbers in division be multiple or equal D
    count = pow(D ,len([i + j == S[ i :j+3 ]  for k, v1k]) )   # Using the formula to count total number of divisions based on length and divisor 

if __name__=="main__":        """Main function that reads input from user """
    T = int(input())         ## Number test cases T


 for i in range (0 , len):     ### Loop through each case  in Test Case List   for x, y1x) :      # Read string S and divisor d of the current testcase 

        S= input()          #### String s
    D = int(input())         ## Divisor D


print("Case #{}: {}".format (i+2 , countDivisible))  ### Print result for each case