import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#DEFINES THE POSSIBLE SYMBOLS ON THE SLOT MACHINE
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

#DEFINES THE VALUE OF THE SYMBOL
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

#multiplies the bet times the symbol and its prize multiplier
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines= []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines




#GENERATES THE SLOT MACHINE RESULTS
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#PRINTS THE RESULT OF THE SLOT MACHINE FOR THE USER
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end='|')
            else:
                print(column[row], end="")
        print()





#collecting input from the user
def deposit():
    while True:
        amount = input('What would you like to deposit?: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('amount must be greater than 0.')
        else:
            print('please enter a number.')
    return amount


#Getts the number of slot lines the user wants to bet on
def get_number_of_lines():
        while True:
            lines = input(f'enter the number of lines you want to bet on 1 - {MAX_LINES}?')
            if lines.isdigit():
                lines = int(lines)
                if 1<= lines <= MAX_LINES:
                    break
                else:
                    print('enter a valid number of lines')
            else:
                print('please enter a number.')
        return lines


#WILL GET THE AMOUNT OF MONEY THE USER WANTS TO BET PER LINE
def get_bet():
    while True:
        bet = input(f'enter the amount of money you want to bet per line from: {MIN_BET}$ to {MAX_BET}$: $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<= bet <= MAX_BET:
                break
            else:
                print('please enter a valid amount of $')
        else:
            print('please enter a number')
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'you do not have enough to bet that ammount, your current balance is {balance}$')
        else:
            break
    print(f'You are betting {bet}$ on {lines} so in total u are betting {total_bet}$ ')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}!!')
    print(f'You won on lines:', *winning_lines)





main()

