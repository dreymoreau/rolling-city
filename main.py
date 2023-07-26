# constant value that will change, capitals for convention
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


# gets the deposit from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # checks if input is a positive number
        if amount.isdigit():
            # by default the input will be a string, this is reassigning the amount from the input into a integer
            amount = int(amount)
            if amount > 0:
                # break out of the while look if the amount inputted is greater than 0 and go straight to return statement
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        #  adding max lines inside and converting to a string, space is off by one space after the question
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        # checks if input is a positive number
        if lines.isdigit():
            #    assigning lines to be a digit
            lines = int(lines)
            # if lines is greater than equals to 1 and less than or equal to MAX_LINES break
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        #  asking user what they want to bet on each line
        amount = input("What would you like to bet on each line? $")
        # checks if input is a positive number
        if amount.isdigit():
            #    assigning lines to be a digit
            amount = int(amount)
            # if lines is greater than equals to 1 and less than or equal to MAX_LINES break
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # template string using the f string
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    # the $ isnt required here like js with template strings, just a way to output dollar amount
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )


main()
