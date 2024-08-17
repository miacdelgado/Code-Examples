import random 

WORDS = ("Algorithm", "Variable","Complier","Debugging", "Database", "Encryption", "Loop", "Boolean", "Function", "Recursion")
HINTS = ("Step-by-step procedure.", "Storage for data", "Translates code into machine language", "Fixing code Error", "Organised data storage","Securing information", "Repeats instruction", "True/False data type","Block of reusable", "Function calling itself")

index = random.randint(0, len(WORDS)-1)
word = WORDS[index]
hint =HINTS[index]

print(word)
correct = word
jumble = ""

score = 0
attempt = 3

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(f"The Jumble: {jumble}")

while attempt > 0:
    guess = input('\nYour guess: ').strip()
    if guess.lower() == correct.lower():
        score += 2
        print(f"You are right you scored {score}")
        break
    else: 
        attempt -= 1
        print("Sorry, that's no it !")

        if attempt > 0:
            help = input("Do you an Hint? (Type Y for yes and N for no): ").lower()
            if help == "y":
                print(f"Hint: {hint}")
            elif help =="n":
                score += 1
            else:
                print("Invaild response\nTry Again!") 
        score -= 1

if guess.lower() != correct.lower():
    print(f"You've used all attempts.\nThe correct word was: {correct}")
else:
    print(f"Final Score: {score}")
print("Thanks for playing.")


