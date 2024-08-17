import random

characters = "abcedefghijklmnopqrstuvwxyz" +"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"0123456789"+"@#₹&!?*=%€¥$¢"
vish = int(input("Enter the length of password you like: "))                                                
if vish != 0:          
    print("The Generated Password of length " + str(vish) +" is")
    for _ in range(vish):                                      
        print(random.choice(characters), end="")
else:
    print("The value entered is not valid.")
