from unittest.mock import MagicMock

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

    def test_view_shows_list_of_dishes_with_prices(capsys):
        dish1 = MagicMock()
        dish1.name = "Apple"
        dish1.price = 2

        dish2 = MagicMock()
        dish2.name = "Banana"
        dish2.price = 3
        
        menu = Menu()
        menu.dishes = [dish1, dish2]
        
        list = menu.view()

        assert "Apple" in list[0]
        assert "£2" in list[0]
        assert "Banana" in list[1]
        assert "£3" in list[1]