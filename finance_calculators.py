import math

''' Objective of the program is to help the user access two different
fincancial calculators, investment calculator and home repayment calculator'''

# Request user to choose between bond or investment calculators
# Create variables for bond and investment
# Get input from the user
# Use if else statements to calculate
# Print out the calculations based on users choices


investment = print("To calculate the amount of interest you will earn on your investment")
bond = print("To calculate the amount you will have to pay on an home loan")

selection = input("Enter 'investment' or 'bond' from the menu above to proceed: ").lower()
 
if selection == "investment":
    amount = int(input("Deposit: "))
    interest_rate = int(input("Interest rate: "))
    years = int(input("Years of investment: "))         
    interest = input("Compound or Simple: ").lower()
    
# The interest rate entered must be divided by 100 
    if interest == "simple":
        simple = amount *(1 + (interest_rate / 100)*years)    
        simple1 = (round(simple, 2))
        total_simple = "With {} deposit you will recieve R{} after {} years at an interest rate of {}%.".format(amount, simple1, years, interest_rate )
        print(total_simple)
        
    elif interest == "compound":
        compound = amount * math.pow(1 +(interest_rate / 100), years)
        compound1 =(round(compound, 2))
        total_compound = "With {} deposit you will recieve R{} after {} years at an interest rate of {}%.".format(amount, compound1, years, interest_rate)
        print(total_compound)
        
# The interest rate entered for bond must be divided by 100, then divided by 12 to get the monthly interest
elif selection == "bond":
    house_value = int(input("House value: "))
    bond_interest_rate = int(input("Interest rate: " ))
    bond_interest_rate1 = (bond_interest_rate / 100 )       
    bond_interest_rate2 = (bond_interest_rate1 / 12 )                                                              
    num_months = int(input("how many months to repay: " ))
 
    bond_repayment = (bond_interest_rate2 * house_value)/(1 -(1 + bond_interest_rate2)**(- num_months))
    bond_repayment1 = round(bond_repayment, 2)
    bond_repayment_value = "You will repay {} every month".format(bond_repayment1)
    print(bond_repayment_value)
    
else:
    print("Please enter the correct selection ")
    