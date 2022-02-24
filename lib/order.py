

class Order():
    def __init__(self):
        self.dishes = []
    
    def add(self, dish):
        self.dishes.append(dish)
    
    def summary(self):
        self.list()
        self.total()
    
    def list(self):
        print([f"{dish.name} .... £{dish.price}" for dish in self.dishes])
    
    def total(self):
        total = sum([dish.price for dish in self.dishes])
        print("Total: £", total)
