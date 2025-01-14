class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                 description:str,
                 processor_type:str,
                 hard_drive_capacity:int,
                 memory:int,
                 operating_system:str,
                 year_made:int,
                 price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def get_year(self): #outputs the year model of a computer
        return self.year_made
    def set_price(self, price:int): 
        self.price = price #changes price
    def update_OS(self, new_OS:str):
        self.operating_system = new_OS #changes operating systems
    def get_description(self): #model of a computer
        return self.description 
    
    