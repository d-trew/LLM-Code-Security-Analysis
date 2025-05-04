def findSmallestString(s):   # Function to return smallest string after highlighting letters in a given input s      return ''.join([ch * (2 if ch == letter else) for i, l  in enumerate(''. join((sorted)))]) 

T = int() # Number of test cases
for t_index range T:    s=input().strip())   # Input string from each case     print(f'Case #{t+1}: {findSmallestString ( s)}')