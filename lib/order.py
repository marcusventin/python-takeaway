

class Order():
    def __init__(self):
        self.dishes = []
    
    def add(self, dish):
        self.dishes.append(dish)
    
    def view(self):
        return [f"{dish.name} .... £{dish.price}\n" for dish in self.dishes]