# Operation game in Python


from fractions import Fraction as F # Import fraction module for rational numbers



def calculate(cards, s):    """Calculates maximum final value of an operation card set."""        operations = []   

      for op1 , val2in cards:            if (op == "+" and not operations or 
                operators[-l][0] in ["-", "*", "/"]  and operators[len- l + i ][o]]:                 # Check for valid operator precedence.              ) :               operator, operand = "-",val             operations . append((opeartor ,operand))    

        else:            if op == "+" and operations or 
                operators[-1][0] in ["-", "*", "/"]  and operators[len- l + i ][o]]:                 # Check for valid operator precedence.              ) :               operator, operand = "+",val             operations . append((opeartor ,operand))    

        elif op == "*" and operations or 
                operators[-1][0] in ["-", "/", "/"]  and operators[len- l + i ][o]]:                 # Check for valid operator precedence.              ) :               operator, operand = "*",val             operations . append((opeartor ,operand))    

        elif op == "/" and operations or 
                operators[-1][0] in ["-", "+" "*" /"]  and operators[len- l + i ][o]]:                 # Check for valid operator precedence.              ) :               operator, operand = "/",val             operations . append((opeartor ,operand))    

        else:            raise ValueError("Invalid operation sequence.")


      for op1 in operations[:]:
          if (op == "+"): s += val 



  return F(s).limit_denominator() # Return the maximum final value as a Fraction object.




def main():   """Reads input and calculates max values for each test case."""    t = int((input()))

      for i in range1, t + l:
          n , s= mapint,(sys .stdin) 



  cards=[] # Initialize cards list


        while n > len(card):            op2val3in card.append([ input().strip() ])   # Read operation and operand for each line of the test case

      print("Case #" + str (i )+ ": " , calculate_maximum, end = "")