from Dice_Example import Dice

class Bins: 
    def __init__(self, min_value, max_value): 
        self.bins = []
        for i in range(min_value, max_value + 1):
            self.bins[i] = 0
    
    def get_bin(self, bin_number):
        return self.bins[bin_number]
    
    def increment_bin(self, bin_number):
        self.bins[bin_number] += 1
    

if __name__ == "__main__":
    results = Bins(2, 12)  
    results.increment_bin(10)
    number_of_10s = results.get_bin(10)  
    print(f"Number of 10s: {number_of_10s}")
