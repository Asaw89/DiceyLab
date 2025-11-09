import random

class Dice:
    def roll(self):
        return random.randint(1, 6)
    
    def toss_and_sum(self):
        n = int(input("How many dice? "))
        total = sum(self.roll() for i in range(n))
        return total

dice = Dice()
toss = dice.toss_and_sum()
print(f"You rolled {toss}")