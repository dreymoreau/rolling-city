# gets the deposit from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # checks if input is a positive number
        if amount.isdigit():
            # by default the input will be a string, this is reassigning the amount from the input into a integer
            amount = int(amount)