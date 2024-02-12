from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = [] # Computer objects will go in here
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    # What methods will you need?
    def buy(self, newComputer:Computer):
        name = newComputer.get_description()
        print(f"Buying {name}...")
        self.inventory.append(newComputer)
        print("Done.")
        print(self.inventory)
        # 1. Call computer(..) constructor to create a new computer instance
        # 2. call inventory.append(...) to add the new computer instance to the inventory
    def sell(self, newComputer:Computer):
        if newComputer in self.inventory:
            name = newComputer.get_description()
            print(f"Selling {name}...")
            self.inventory.remove(newComputer)
            print("Done.")
            print(self.inventory)
        else:
            return False    
    def refurbish(self, newComputer:Computer):
        if newComputer in self.inventory:
            print("Updating...")
            if newComputer.get_year() < 2000:
                newComputer.set_price(0)
            if newComputer.get_year() < 2012:
                newComputer.set_price(250)
            if newComputer.get_year() < 2018:
                newComputer.set_price(550)        
            else:
                newComputer.set_price(1000)
        else:
            print(f"{newComputer} not found. Please select another item.")        
#running to check if code works
def main():
    compOne = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    compTwo = Computer("2019 MacBook Pro", "Intel",
                       256, 16, "High Sierra", 2019, 1000)
    ResaleShop().buy(compOne)
    ResaleShop().buy(compTwo)

main()