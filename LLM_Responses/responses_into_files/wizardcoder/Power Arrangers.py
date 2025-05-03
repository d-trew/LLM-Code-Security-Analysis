T = int(input()) # Read number of test cases
F = int(input()) # Read maximum number of figures to inspect per test case
for i in range(T):
    missing_set = input() # Input the letter arrangement of the missing set
    for j in range(F+1):
        if j == F:
            print("Missing set is", missing_set) # Output the missing set after checking all figures
            break
        else:
            fig = input() # Input a figure from left to right
            if fig not in missing_set:
                print(fig) # Output the letter of the current figure