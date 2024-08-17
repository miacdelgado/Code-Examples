userDecision = input("Do you want to play? ")

if userDecision.lower()  != "yes":
    quit()
    
print("Let's start playing then ??")



quiz_questions = [
    {"question": "What is Python?", "answer": "A high-level programming language"},
    {"question": "What are comments used for in Python?", "answer": "To add explanatory notes to code"},
    {"question": "What is the difference between class method and instance method? ", "answer": "Class method: bound to class, Instance method: operates on instance" },
    {"question": "What is OOP?", "answer": "Object-oriented programming" },
    {"question": "What is the difference between set and dictionary?", "answer": "Set: unique elements, Dictionary: key-value pairs" },
    {"question": "What is recursion? ", "answer": "Function calls itself to solve a problem" },
    {"question": "What does 'DRY' stand for in programming? ", "answer": "Don't Repeat Yourself"},
    {"question": "What is the difference between list and tuple?", "answer": "List: mutable, Tuple: immutable"},
    {"question": "What is the purpose of the `if` statement in Python? ", "answer": "Conditional execution based on conditions"},
    {"question": "What is tifference between `==` and `is` in Python?", "answer":  " `==` compares values, `is` checks memory location"},
    {"question": "What is a function? ", "answer": "Reusable block of code performing a task" },
    {"question": "What is the purpose of `range()` function? ", "answer": "Generates a sequence of numbers"},
    {"question": "WhaT is the difference between local and global variables? ", "answer": "Local: inside functions, Global: accessible anywhere"},
    {"question": "What is the purpose of `try-except` block?", "answer": "Handling errors or exceptions"}
]


import random
random.shuffle(quiz_questions)


def display_question(question):
    print(question)
   
def get_answer():
    answer = input("Enter your answer: ")
    return answer
    
score = 0          
           
for question in quiz_questions:
    display_question(question["question"])
    user_answer = get_answer()
        
    if user_answer.casefold() == question["answer"].casefold():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")
 
print("Quiz completed!")
print(f"Your score: {score}/{len(quiz_questions)}")