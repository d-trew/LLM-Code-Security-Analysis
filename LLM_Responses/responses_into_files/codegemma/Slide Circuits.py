# Sample Case #0.txt   


def findDisabledSlide(operations):    	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1

B, S = map (int,(input().split())) 



slides_enabled= [False] *S  
circuits=[]   


for _ in range(0 , B):    	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1

cir = set()                          # circuit is a list of buildings connected by enabled slides 



def add_toCircuit (a,b) :   
  if b not in cir:    	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1

cir.add( a )                       # circuit is updated with new building 


def remove_fromCircuit (a) :   
  if len([i for i in cir if not slidesEnabled[ listofSlideNumbers [list of Building numbers].index()]]) ==0:    	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1

cir.remove( a )                       # circuit is updated with new building 



for _ in range (S):  
 listofSlideNumbers = map int, input().split()   	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1

list of Building numbers=map(int,(input())) 



for i in range (N):  
 op_type , l = map((str, int), input().split())   	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1

if len([i for j>l and slidesEnabled[j] ]) ==0:    
  print('X', end=' ') 


else : print( listofSlideNumbers [list of Building numbers].index()] )   	     		      			       				        					          						            							         								             									               										           												                 											                             ##Sample case ##1