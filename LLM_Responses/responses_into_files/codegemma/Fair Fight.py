def countFairFights():    # Function to calculate the number of fair fights.   N = int()     K=int(); CharlesSkillLevels=[] ; DelilaSkillsLevel =[]  for i in range(0, N):        Charlesskilllevels[i] += (input())      Delilaskilllevel [:] + input().split()]
    countOfFairFightsCountEachPairWithInGivenRange = 1; # Initialize the count of fair fights.   # Iterate over all pairs from L to R and check if fight is fairly balanced between Charles's skill level with his chosen sword type, Delila’skill levels on her selected swords types are within K range
    for i in list(range (L ,R+1)):        countOfFairFightsCountEachPairWithInGivenRange += 

            max([CharlesSkillLevels[i-l] - max [Delilaskilllevel[:]] for l  in DelilaSkillsLevel]) <=K and min ([ Charlesskilllevels.index,delilahskills level ]) >= K)
    return countOfFairFightsCountEachPairWithInGivenRange;


if __name__ == '__main__':

     T = int(input()) # No of test cases to be run 



for i in range (1 , T+2):  # Run the loop for each Test case.   N, K= map((int), input().split()); CharlesSkillLevels=[] ; DelilaSkillsLevel =[]
    Charlesskilllevels=[ ] + list(map (( int ),input (). split())) # Skill levels of charles 

delilahskillslevel = []+list (  # skill level for delia.   for i in range [0, N] :        DelilaskillLevels[i]=int()