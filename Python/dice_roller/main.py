import random
import class_a

amount_of_rolls = int(input('How many times would you like to roll the die? '))
my_die = class_a.Die()
for i in range(amount_of_rolls):
    print(my_die.roll())