from unittest.mock import MagicMock
from random import randint

from lib.menu import Menu

class TestMenu():
    def test_add_adds_dish_to_menu(self):
        dish1 = MagicMock()
        dish2 = MagicMock()

        menu = Menu()
        menu.add(dish1)
        assert dish1 in menu.dishes

        menu.add(dish2)
        assert dish1 in menu.dishes
        assert dish2 in menu.dishes

    def test_list_shows_all_dishes_and_prices(self, capsys):
        rand1 = randint(1, 100)
        rand2 = randint(1, 100)
        
        dish1 = MagicMock()
        dish1.name = "Apple"
        dish1.price = rand1

        dish2 = MagicMock()
        dish2.name = "Banana"
        dish2.price = rand2
        
        menu = Menu()
        menu.dishes = [dish1, dish2]

        menu.list()

        out = str(capsys.readouterr())
        assert "Apple" in out
        assert str(rand1) in out
        assert "Banana" in out
        assert str(rand2) in out