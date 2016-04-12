#Calendar App
#Author: Robert Koehler
#Date: 4/11/15

#import calLIb

menuSelection = -1

while menuSelection == -1:

    print('Main Menu:')
    print()

    print('1. Add a New Event')
    print("2. View Today's Schedule")
    print('3. View Future Events')
    print('4. Manage Events')
    print('5. Exit Program')

    menuSelection = int(input('Please selecct a number:'))

    if menuSelection >=1 and menuSelection <=4:
        print('Need more input')
    elif menuSelection == 5:
        print("You stay classy San Diego!")
    else:
        print("That was not a number between 1 and 5. Please try again.")
        menuSelection = -1