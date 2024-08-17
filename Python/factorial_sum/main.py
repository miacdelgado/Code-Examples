# This imports the functions from the repetition.py file
import repetition

# This part of the code creates a menu for the user to user
print('Find the Factorial or Sum of all Odd numbers\n'
      '1-Factorial\n'
      '2-Sum Odd Numbers\n'
      '3-Exit\n'
      'Note: Invalid choice will close the program')

# Prompts the user for one of the menu item selects
menu_select = int(input('Select one of the above options: '))

# Would probably need a while loop to check for input 1 or 2 or 3
while menu_select == 1 or menu_select == 2 or menu_select == 3:

    # The following if statement runs if the user selects option 1
    if menu_select == 1:

        # Prompts the user for a number to calculate the factorial for
        factorial = int(input('Please enter the number you would like to get the factorial of (between 0-10): '))

        # Requests a new number from the user within range if the number from before was out of range
        while factorial <0 or factorial > 10:
            factorial = int(input('That number is not valid, please choose a number between 0-10: '))

        # Calculates the factorial and returns the result
        result = repetition.get_factorial(factorial)
        print('The factorial of the number entered is', result)

        # After printing the requested info, this asks the user if they want to continue using the program
        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'y':
            menu_select = int(input('Please select another choice from the Homework 3 Menu: '))
        else: 
            menu_select = 'exit'

    # The following if statement runs if the user selects option 2
    elif menu_select == 2:

        # Prompts the user for a number to calculate the sum for
        total_sum = int(input('Please enter the number you would like to get the total sum of all odd factors (between 0-100): '))

        # Requests a new number from the user within range if the number from before was out of range
        while total_sum < 0 or total_sum > 100:
            total_sum = int(input('That number is not valid, please choose a number between 0-100: '))

        # Calculates the total sum of odd factors and returns the result
        result = repetition.sum_odd_numbers(total_sum)
        print('The total sum of all odd factors is', result)

        # After printing the requested info, this asks the user if they want to continue using the program
        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'y':
            menu_select = int(input('Please select another choice from the Homework 3 Menu: '))
        else: 
            menu_select = 'exit'

    # The following if statement runs if the user selects option 3
    else:
        menu_cont = input('Are you sure you want to close the program (y or n)? ')
        
        if menu_cont == 'n':
            menu_select = int(input('Please select another choice from the Homework 3 Menu: '))
        else:
            menu_select = 'exit'

# Exit program message on invalid choice or when the user prompts to exit the program
print('The program is exiting, Goodbye.')