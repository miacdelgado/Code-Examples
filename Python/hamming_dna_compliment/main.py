# import functions
import strings

# Creates menu
print('Calculates Hamming Distance and Gives DNA Compliment\n'
      '1-Hamming Distance\n'
      '2-Dna Compliment\n'
      '3-Exit\n')

# Prompts the user for one of the menu item selects
menu_select = int(input('Select one of the above options: '))

while menu_select != 1 and menu_select != 2 and menu_select != 3:
    menu_select = int(input('That choice is not valid, please choose a menu option: '))

while menu_select == 1 or menu_select == 2 or menu_select == 3:
    if menu_select == 1:
        print("This will help you determine the Hamming distance between two DNA strands.")
        dna_1 = input("Please enter the first DNA string you would like to use: ")
        dna_2 = input("Please enter the second DNA string you would like to use: ")

        ham_distance = strings.get_hamming_distance(dna_1, dna_2)
        print("The Hamming distance between those two DNA strands is: ", ham_distance)

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('What else would you like to do?\n'
                  '1-Hamming Distance\n'
                  '2-Dna Compliment\n'
                  '3-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 3:
                print("Goodbye")
                menu_select = 'exit'

    if menu_select == 2:
        print("This will help you figure out the compliment DNA strand.")
        dna = input("Please enter the DNA strand you would like to find the compliment of: ")

        complement_dna = strings.get_dna_complement(dna)
        print("The compliment DNA strand is: ", complement_dna)

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('What else would you like to do?\n'
                  '1-Hamming Distance\n'
                  '2-Dna Compliment\n'
                  '3-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 3:
                print("Goodbye")
                menu_select = 'exit'

    elif menu_select == 3:
        menu_exit = input("Are you sure you would like to exit the program: ")
        if menu_exit == 'Y' or menu_exit == 'y':
            print("Goodbye")
            menu_select = 'exit'
        else:
            print('What else would you like to do?\n'
                  '1-Hamming Distance\n'
                  '2-Dna Compliment\n'
                  '3-Exit\n')
            
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 3:
                print("Goodbye")