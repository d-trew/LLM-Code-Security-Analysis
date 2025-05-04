from collections import defaultdict


def calculateCompetitionInterest(skillLevels):        rows = len ( skilllevels )     cols=len   (( row for r in range  for c, s i n enumerate if isinstance))      neighbors=[defaultdict() {r:c} ] * rows] 

          interestLevelofEachRound=[]
         while True :       currentSkillSumOfAliveCompetitors = sum(skilllevels[i][j])   if any ( skillLevels ) else  break        for i in range    rows     in enumerate           neighbors):      neighborSkills= [ s for r, c] n neighbors if row!=r or col !=c ] 

          averageSkillLevelOfNeighbors=(sum of neighbor skills)/ len(skilllevels[i][j])
         if skillLevels  < average Skill Level Of Neighbors :       del    skills   in enumerate in range ( rows ) and cols)     interestlevelofEachRound.append sum([s for r, c] n neighbors if row!=r or col !=c ])

        totalInterestLevel =sum( interestlevels of each round