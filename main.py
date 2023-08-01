# generate slot machine values randomly, how many items we want in a row and how many lines we want
import random

# constant value that will change, capitals for convention
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    # checking the bets of how many lines the user bet on
    for line in range(lines):
        # we have all the columns, we are storing the first symbol in the symbol variable
        symbol = columns[0][line]
        for column in columns:
            # checking symbol
            symbol_to_check = column[line]
            # checking if the symbol is not equal to the next symbol, break
            if symbol != symbol_to_check:
                break
            # if we didnt break out of the loop meaning that the symbols matched, then go to else statement
        else:
            winnings += values[symbol] * bet

    return winnings


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    # define columns list
    columns = []
    # generate column for all columns
    for _ in range(cols):
        column = []
        # copies list using slice operator to current symbols, colon ignores the fact of any changes to current_symbols wont impact all_symbols
        current_symbols = all_symbols[:]
        # loop through the number of values that we need to generate which is equal to number of rows in slot machine
        for _ in range(rows):
            # picks random value from list
            value = random.choice(current_symbols)
            # removes value so we dont pick it again
            current_symbols.remove(value)
            # pushing the value to column
            column.append(value)
        # add columns to columns list
        columns.append(column)

    return columns


# passing in columns into this function
def print_slot_machine(columns):
    # determine rows based off of columns and get the length of columns
    for row in range(len(columns[0])):
        # print first value at the first row of the column
        # enumerate gives you the index as well as the item
        for i, column in enumerate(columns):
            # maximum index to access the element in the column list
            if i != len(columns) - 1:
                # pipe operator if its in the middle not at the end of the last column
                # end tells the print statement to what to end the line with
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


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
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to be that amount, your current balance is: ${balance}"
            )
        else:
            break

    # the $ isnt required here like js with template strings, just a way to output dollar amount
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
