import os
import time

def new_parameters():
    # Asks the user for budget information and saves in variables
    input_list = []
    print("Please only use numbers within realistic scope.")
    salary = input_list.append(input("How much did you make this month? ")) #0
    rent = input_list.append(input("How much is the total rent? ")) #1
    electricity = input_list.append(input("How much is the total electricity bill? ")) #2
    gas = input_list.append(input("How much is the total gas bill? ")) #3
    water = input_list.append(input("How much is the water bill? "))#4
    food = input_list.append(input("What is your weekly food budget? ")) #5
    savings = input_list.append(input("What percentage would you like to save/invest? ")) #6

    # Puts user input into saved parameters file
    finances_input_file = open('finances_input_file.txt','w')
    for i in input_list:
        finances_input_file.writelines(i + "\n")
    finances_input_file.close()

def calculator():
    # Retrieves saved input from finances input file and stores in a list
    print("Let's calculate your budget.")
    time.sleep(2)
    with open('finances_input_file.txt', 'r') as i:
        parameter_list = i.readlines()
    # Converts strings from list into integers
    for i in range(0, len(parameter_list)):
        parameter_list[i] = int(parameter_list[i])

    # Listing out inputs
    print(f"You made ${parameter_list[0]} dollars this month.")
    housing_costs = parameter_list[1] + parameter_list[2] + parameter_list[3] + parameter_list[4]
    print(f"Your housing cost is ${housing_costs} in total.")
    food_cost = parameter_list[5] * 4
    print(f"Your food costs are ${food_cost}.")
    
    print(f"You previously put that you wanted to save {parameter_list[6]}% of your total pay.")
    savings_rate = float(parameter_list[6] / 100)
    savings_take_out = parameter_list[0] * savings_rate

    # Final value calculations
    print("Here is the final breakdown: ")
    time.sleep(3)
    print(f"Total expenses: ${housing_costs + food_cost}")
    print(f"Savings taken out: ${savings_take_out}")
    tithe_y_n = input("Would you like to tithe for your church? (10%) Y/N ")
    tithe_y_n.upper
    if tithe_y_n == "Y":
        tithe_cost = parameter_list[0] * .10
        leftover = parameter_list[0] - housing_costs - food_cost - savings_take_out - tithe_cost
        print(f"Your leftover money after all costs is: {leftover}.")
    else:
        leftover = parameter_list[0] - housing_costs - food_cost - savings_take_out
        print(f"Your leftover money after all costs is: ${leftover}.")
        if leftover < 0:
            print("Ouch. No money left.")



#! Start of program==================================================================================
print("Welcome to the Monthly Finances Calculator. ")
if os.path.isfile('finances_input_file.txt') == True:
    change_param = input("Would you like to set new parameters? Y/N\n")
    change_param.upper
    if change_param == "Y":
        new_parameters()
        calculator()
    elif change_param == "N":
        print("Ok, we will use your previously saved parameters.")
        calculator()
else:
    print("Let's go through your monthly costs.")
    new_parameters()
    calculator()







