import is_prime

# Asks the user for a number to test is its prime or not
num = int(input("Please enter a number you would like to check to see if its prime: "))

prime = is_prime.is_prime(num)

if prime == True:
    print(num, "is a prime number.")
else: 
    print(num, "is not a prime number.")