# The following function accepts one parameter and returns its factorial
# Factorial: n! = n * (n-1) * ... * 1 
def get_factorial(num):
    # create product variable to contain number entered, this is the starting product
    product = 1

    # Loop that takes the number above and puts in it a range   
    for f in range(1,num+1):

        # update the product variable
        product *= f 

    # Return the value of the product variable
    return product

# The following functions accepts one parameter and returns the sum of all odd numbers up to its value
def sum_odd_numbers(num):
    # create sum variable that starts at 0, this will contain the sum of all numbers
    sum = 0

    # Loop that checks whether the num variable is greater than 1 (1 being the lowest odd number)
    while num >= 1:
        # check to see if num is odd, if so add it to the sum variable
        if num % 2 == 1:
            sum += num 

            # delete 1 from num variable (when current value is odd)
            num -= 1

        # delete 1 from the num variable (when current value is even)
        else:
            num -= 1

    # Return the value of the sum variable
    return sum