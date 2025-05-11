from random import randint



def estimate(N: int) -> float :  # N is number of rooms in cave, returns an estimated value for passages between them with K operations allowed as input.K =8012 # maximum room operation count 


    passages= [randint (3,(4*i))for i range((int)(ceil(N/5))) ]
  # generates random number of connections per each N rooms in cave, where the minimum is three and max four times as many.

   return sum([p for p passages]) / len[passages] # calculates average passage count 



def main():


    T = int (input())     ## T - test case input
  for _ i range(1,(int)(ceil((2/3)*N))): ## K operations allowed in each of the tests cases.

       R, P= map[str] float) # R is current room and p are number pf passages from it 


        if (i==K+4 or input().strip() != "E"):  # checks if operation was estimation
            break   ## exit loop as we have done K operations.

    print(estimate())