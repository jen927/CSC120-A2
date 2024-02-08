from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = [] # Computer objects will go in here
    newComputer: object
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory:list, newComputer:object):
        self.inventory = inventory
        self.newComputer = newComputer
    # What methods will you need?
    def buy(self):
        self.inventory.append(self.newComputer)
        print(self.inventory)
        # 1. Call computer(..) constructor to create a new computer instance
        # 2. call inventory.append(...) to add the new computer instance to the inventory
    def sell(self):
        pass
    def refurbish(self):
        pass

#running to check if code works
def main():
    newComputer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    computerOne = ResaleShop(inventory,)

main()