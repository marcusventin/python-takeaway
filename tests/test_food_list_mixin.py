from unittest.mock import MagicMock
from random import randint

from lib.food_list_mixin import FoodListMixin

class TestFoodListMixin():
    def test_add_adds_dish_to_dishes(self):
        dish1 = MagicMock()
        dish2 = MagicMock()

        subject = FoodListMixin()
        subject.add(dish1)
        assert dish1 in subject.dishes

        subject.add(dish2)
        assert dish1 in subject.dishes
        assert dish2 in subject.dishes

    def test_list_shows_all_dishes_and_prices(self, capsys):
        rand1 = randint(1, 100)
        rand2 = randint(1, 100)
        
        dish1 = MagicMock()
        dish1.name = "Apple"
        dish1.price = rand1

        dish2 = MagicMock()
        dish2.name = "Banana"
        dish2.price = rand2
        
        subject = FoodListMixin()
        subject.dishes = [dish1, dish2]

        subject.list()

        out = str(capsys.readouterr())
        assert "Apple" in out
        assert str(rand1) in out
        assert "Banana" in out
        assert str(rand2) in out