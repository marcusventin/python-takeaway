from random import randint

from lib.dish import Dish

class TestDish():
    def test_dish_has_a_user_defined_price(self):
        random_number = randint(1, 100)
        dish = Dish(random_number)
        assert dish.price == random_number