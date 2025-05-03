T = int(input()) # number of test cases
for i in range(1, T+1):
    N, M = map(int, input().split()) # read the number of courses and the number of cool words
    courses = {} # dictionary to store prerequisites for each course
    
    for j in range(N):
        line = input()
        if line[1] == 'B': # basic course
            courses[line[0]] = []
        else: # advanced course
            prereq, adv_course = line.split()
            courses[adv_case] = [prereq]
    
    for j in range(M):
        cool_word = input().strip()
        
        count = 0 # number of valid sequences that contain the cool word as a substring
        total_count = 0 # total number of possible sequences
        
        for key, value in courses.items():
            if len(value) == 1: # only one prerequisite
                prereq = value[0]
                count += 1 # start with the prerequisite and continue with the course that has no prerequisites
                
                for k in range(len(cool_word)):
                    if cool_word[k] == key:
                        total_count += 2**(N-1) # since we start with a prereq, there are always two ways to complete the remaining courses (with or without it)
            
            elif len(value) == 0: # no prerequisites
                for k in range(len(cool_word)):
                    if cool_word[k] == key:
                        total_count += 1
        
        print("Case #{}: {}".format(i), end="")
        for j in range(M):
            count = float(count) / total_count # calculate the fraction of valid sequences that contain the cool word as a substring
            if count >= 0.97 and count <= 1.03: # within an absolute error of 0.03
                print(" {:.6f}".format(count), end="")
            else:
                print(" {:.5f}".format(count), end="")
        print()