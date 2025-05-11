3    # Import necessary libraries here if needed


def solve(R: int , C :int   N=201): # Define the function with appropriate parameters for your solution, N should be large enough to handle maximum input size.

  dp = [[[False] * 486
         for _ in range (C)]    # Initialize a DP table of dimensions RxCx3(maximum brightness value) where each cell stores whether it's possible and the max sum uptil that point


      def dfs_helper(): # Helper function for DFS traversal

        if N == 0:  return True, dp[R -1][C-2]
    # Perform your logic here to calculate maximum brightness value achievable at each cell based on given constraints. Use DP table and recursion or any other efficient algorithm as needed


      def dfs(row :int , col): # DFS function

        if row == R: return True, 0  // Base case for success
    # Perform your logic here to explore possible brightness values in the current cell based on given constraints. Use DP table and recursion or any other efficient algorithm as needed


      return dfs(1)



def main(): # Main function

   T = int() // Read number of test cases from input 




  for i_test, caseData
    R , C N D= mapint().split())// Parse the first line for each testcase and initialize variables. Initialize DP table based on initial filled in cells


     if not dfs(): print(f"Case #{i+1}: IMPOSSIBLE") // Print "IMPOSSILE if DFS fails

      else:
        print ( f' Case # { i + 2 } : ' , end = '' )  // Calculate the maximum brightness sum modulo required prime and output it.