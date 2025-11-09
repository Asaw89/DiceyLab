import random

class Bin:
    def __init__(self, min_value, max_value): 
        self.bins = []
        for i in range(min_value, max_value + 1):
            self.bins.append(0)
    
    def get_bin(self, bin_number):
        return self.bins[bin_number-2]
    
    def increment_bin(self, bin_number):
        self.bins[bin_number-2] += 1


class Dice:
    def __init__(self,numberOfDice, numberOfSides):
        self.numberOfDice = numberOfDice
        self.numberOfSides = numberOfSides


    def roll(self):
        return random.randint(1, self.numberOfSides)
    
    def toss_and_sum(self, numberOfDice):
        total = sum(self.roll() for i in range(numberOfDice))
        return total


class Simulation:
    def __init__ (self, numberOfDies, numberOfTosses, numberOfSides):
        self.numberOfDies = numberOfDies
        self.numberOfTosses = numberOfTosses
        self.numberOfSides = numberOfSides
        self.dice = Dice(numberOfDies, numberOfSides)
        self.results = Bin(numberOfDies, numberOfDies* numberOfSides)

    def run_simulation(self):
        for i in range(self.numberOfTosses):
            toss = self.dice.toss_and_sum(self.numberOfDies)
            self.results.increment_bin(toss)
    
    def print_results(self):
        for i in range(self.numberOfDies,self.numberOfDies*self.numberOfSides+1):
            pct=self.results.get_bin(i)/self.numberOfTosses
            print(f"{i:2}: {self.results.get_bin(i):8}: {pct:.2f} ",end="")
            for j in range(0,(int)(pct*100)):
                print("*",end="")
            print("")
        
        

    


if __name__ == "__main__":
    sim = Simulation(2, 1000000,6)
    sim.run_simulation()
    sim.print_results()