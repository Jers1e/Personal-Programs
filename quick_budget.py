def budget_calculator(income, *expenses):
    """Takes total monthly income, and minuses all expenses (unlimited arguments) and divides it by 2,
     splitting evenly between savings account and investing"""
    
    #All expenses arguments are in a tuple, and get added to the total_expenses variable, they then
    # get subtracted from the income argument, and are stored in another variable and divided by 2
    # to simulate splitting the remaining money between saving and investing
    total_expenses = 0
    for i in expenses:
        total_expenses += i
    left_over = float(income) - float(total_expenses)
    save_and_invest = left_over / 2

#Values here are all rounded for simplicity
    if left_over == 0:
        print("You have no money leftover!")
    elif left_over < -.01:
        print("You have no money to invest!")
        print(f"You are ${round(left_over)} in debt!")

    else:
        print(f"Out of ${round(income)}, you have ${round(left_over)} remaining, you should put ${round(save_and_invest)} in both savings and investments.")


#? Input values here!
budget_calculator(1600.25, 800.69, 300)