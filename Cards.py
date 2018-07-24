# Reference to:
# [1] Valentyn N Sichkar. Implementing game with cards in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/playing_cards_in_Python (date of access: XX.XX.XXXX)


# Implementing the task
# Playing card's game

# Creating a list to store the suits of the cards
# Clubs, diamonds, hearts, spades
lst_suits = ['C', 'D', 'H', 'S']

# Creating a list to store the values of each card
# 6, 7, 8, 9, 10, J, Q, K, A
lst_values = ['6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']

# Inputting two cards in one line divided by gap
cards = input().split(' ')  # Result will be a list with two cards ['AH', 'JH']

# Deleting '0' if value of the card is '10' in order to keep all cards with two elements only
if '0' in cards[0]:
    cards[0] = '1' + cards[0][2]
if '0' in cards[1]:
    cards[1] = '1' + cards[1][2]

# Inputting suit of the game
suit = input()

# Checking if the first card has suit of the game
if cards[0][1] == suit:
    # Checking if the second card also has suit of the game
    if cards[1][1] == suit:
        # Checking which one has higher value
        if lst_values.index(cards[0][0]) > lst_values.index(cards[1][0]):
            print('First')
        else:
            print('Second')
    # If the second card doesn't have suit of the game
    else:
        print('First')

# Checking if the second card has suit of the game
elif cards[1][1] == suit:
    # Checking if the first card also has suit of the game
    if cards[0][1] == suit:
        # Checking which one has higher value
        if lst_values.index(cards[0][0]) > lst_values.index(cards[1][0]):
            print('First')
        else:
            print('Second')
    # If the first card doesn't have suit of the game
    else:
        print('Second')

# If both don't have suit of the game
else:
    # Checking if the cards have the same suit
    if cards[0][1] == cards[1][1]:
        # Checking which one has higher value
        if lst_values.index(cards[0][0]) > lst_values.index(cards[1][0]):
            print('First')
        else:
            print('Second')
    # If cards have different suits
    else:
        print('Error')
