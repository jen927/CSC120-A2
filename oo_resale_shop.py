from computer import *
from typing import Dict, Optional

class ResaleShop:

    # What attributes will it need?
    inventory = [] # Computer objects will go in here
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory:list):
        self.inventory = inventory
        
    # What methods will you need?
        
    # adds computer to inventory    
    def buy(self, newComputer:Computer):
        name = newComputer.get_description()
        print(f"Buying {name}...")
        self.inventory.append(newComputer)
        print("Done.")
        
    # removes computer from inventory
    def sell(self, newComputer:Computer):
        if newComputer in self.inventory: #checks if computer exists in inventory
            name = newComputer.get_description() # gets the description of the computer
            print(f"Selling {name}...")
            self.inventory.remove(newComputer) # removes it from inventory
            print("Done.")
        else:
            return False 

    #updates price and operating system       
    def refurbish(self, newComputer:Computer, new_os: Optional[str] = None):
        if newComputer in self.inventory:
            name = newComputer.get_description()
            print(f"Updating {name}...")
            if newComputer.get_year() < 2000: #too old to sell. Only donation
                newComputer.set_price(0)
            elif newComputer.get_year() < 2012: # heavily-discounted price on machines 10+ years old
                newComputer.set_price(250)
            elif newComputer.get_year() < 2018: # discounted price on machines 4-to-10 year old machines
                newComputer.set_price(550) 
            else:
                newComputer.set_price(1000) # recent stuff
            if new_os is not None: #updates operating system if one is listed
                newComputer.update_OS(new_os)
            print("Done.")        
        else:
            print(f"{newComputer} not found. Please select another item.")        
#running to check if code works
def main():
    #created two computers
    compOne = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    compTwo = Computer("2019 MacBook Pro", "Intel",
                       256, 16, "High Sierra", 2019, 1000)
    #bought both computers
    bought = ResaleShop([])
    bought.buy(compOne)
    bought.buy(compTwo)
    #refurbished computers
    bought.refurbish(compOne)
    bought.refurbish(compTwo, "MacOS Monterey")
    #selling computer
    bought.sell(compTwo)
    
main()