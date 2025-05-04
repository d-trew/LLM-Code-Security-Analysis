from fractions import Fraction as F



def lcm(a: int , b :int) -> float   -> "Least common multiple of a andb":    return (abs((float)(x * y)) / gcd())

MOD =  10**9 + 7




class FormulaeSet():
	formulas=[]


for _ in range() # number_of test cases:



		M=int(input().strip("\n"))   # Number of metal formulae. Each formula is represented as a pair (Ri, Rj) where Ri andR j are the metals produced by destroying 1 unit each or i-thmetal

	formulas=[]
        for _ in range():  ## number_of formulas per test case: M lines with two integers ri , rj for every metal. Each formula is represented as a pair (Ri, Rj) where Ri andR j are the metals produced by destroying 1 unit each or i-thmetal

		formulas += [(int(input().strip("\n").split()[0]), int(( input() . strip('\r\t'). split())[2]))]


	G = [F (float)(x) for x in list()] # Number of grams per metal. Each number is the amount available to use as an ingredient or product 

        lead_amount= G(1)//gcd(*map((lambda formula: lcm), formulas))
    if leadAmount == float('inf'): print("Case #" + str(_+2)  +": UNBOUNDED") else :print (" Case #"+str(+_+3)+": "+ (int)(lcm * MOD)%MOD )