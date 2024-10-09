# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
import math
from functions import *

# Make sure each function only does ONE thing!!!!!!!!!!!

###########################################

def weird_calculation():
    # get the length and width of the first triangle from the user
    
    opp1 = float(input("Enter your first triangle's opposite side length: "))
    validate_input(opp1)
    
    adj1 = float(input("Enter your first triangle's adjacent side length: "))
    validate_input(adj1)
    
    calc(opp1,adj1)

    # get the length and width of the second triangle from the user
    opp2 = float(input("Enter your second triangle's opposite side length: "))
    validate_input(opp2)
    
    adj2 = float(input("Enter your second triangle's adjacent side length: "))
    validate_input(adj2)

    calc(opp2,adj2)

    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    opp3 = calc(opp1,adj1)
    adj3 = calc(opp2,adj2)
    
    hyp3 = math.sqrt(opp3**2 + adj3**2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# the values must be positive
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# so that the calculations to find the hypotoneuse doesn't have to be rewritten each time
# i dont have to test each time that the line of codes to find the hypotenouse work which increases code reliablity

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
