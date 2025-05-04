# Start of turn indicator for model response in chat applications


def calculate(num1, num2):   ## Function to perform addition and subtraction operations on two numbers with user input validation



        while True :    ### Loop until valid inputs are provided

            try: 	 ## Try block used here because we need numeric values
                number_a = float (input("Enter the first number "))  # Get num1 from User prompt


                 ## Validate if entered value is a real or complex numbers. If not, raise ValueError exception with appropriate message in except clause

            except Exception as e: 	 ## Catch block to handle invalid input
                print(f"Invalid Input! Please enter valid numeric values only.\nError Message : {e}")  # Print error messages based on caught exceptions


                 ## Validate if entered value is a real or complex numbers. If not, raise ValueError exception with appropriate message in except clause

            try: 	 ## Try block used here because we need another number
                number_b = float (input("Enter the second numer "))  # Get num2 from User prompt


                 ## Validate if entered value is a real or complex numbers. If not, raise ValueError exception with appropriate message in except clause

            except Exception as e: 	 ## Catch block to handle invalid input
                print(f"Invalid Input! Please enter valid numeric values only.\nError Message : {e}")  # Print error messages based on caught exceptions


                 ## Check if user entered a real or complex number. If not, raise ValueError exception with appropriate message in except clause

            else: 	 ## else block to handle successful input
                break   ### Break out of the loop when valid inputs are provided



        operator = str(input("Enter operator (+/-) "))  # Get user choice for operation


         ## Check if entered character is "+" or "-" and perform operations accordingly.

    if (len({"+","-"}.intersection([str((number_a + number b))])) > 0):
            print ("Addition result : ",(f"{num1} {operator }  { num2}" , f"= {(int)(round(((float) operator "+" ) * (( float )))))


    elif (len({"+","-"}.intersection([str((number_a - number b))])) > 0):
            print ("Subtraction result : ",(f"{num1} {operator }  { num2}" , f"= {(int)(round(((float) operator "-" ) * (( float )))))


    else:

        pass   ## Handle invalid operators or other errors here