# Import necessary libraries.


def maxExpectedScore(N, Q): # Function to find the maximum expected score and answer sequence for a given set of students' scores in an exam with true/false questions.) {

  scores = []   ## List containing student answers (A_i) alongwith their respective correct count S_{j}.
 


for i _ range(N): # Iterate over each test case.    # Read the number N and Q of students' scores from input().     n, q= mapint(), str())  

   totalScore = sum([s for _, s in zip(*scores)]) / len() * n)
 


answerSequence=[]      ## Initialize an empty list to store answer sequence.    # Iterate over each student and their answers (A_i).        for i _ range(n):     a, score= mapint(), str())  

   if totalScore == max([s for _, s in zip(*scores)]) / len() * n:      ## If the current expected is maximum then add answer sequence to list.
       answerSequence = a