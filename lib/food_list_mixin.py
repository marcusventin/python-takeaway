class FoodListMixin:
    def __init__(self):
        self.dishes = []
    
    def add(self, dish):
        self.dishes.append(dish)
    
    def list(self):
        print([f"{dish.name} .... £{dish.price}\n" for dish in self.dishes])