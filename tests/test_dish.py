from random import randint

from lib.dish import Dish

class TestDish():
    def test_dish_has_a_user_defined_name_and_price(self):
        random_number = randint(1, 100)
        dish = Dish('test_name', random_number)
        assert dish.name == 'test_name'
        assert dish.price == random_number