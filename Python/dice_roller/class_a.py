import random

class Die:
    def __init__(self):
        self.roll_history = []

    def roll(self):
        value = random.randint(1,6)
        self.roll_history.append(value)
        return value

    def __str__(self):
        return f"Last roll: {self.roll_history[-1]}"