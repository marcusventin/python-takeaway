from unittest.mock import MagicMock
from random import randint

from lib.order import Order


class TestOrder():
    def test_add_adds_item_to_order(self):
        dish1 = MagicMock()
        dish2 = MagicMock()

        order = Order()

        order.add(dish1)
        assert dish1 in order.dishes

        order.add(dish2)
        assert dish2 in order.dishes
    
    def test_list_shows_list_of_items(self, capsys):
        rand1 = randint(1, 100)
        rand2 = randint(1, 100)
        
        dish1 = MagicMock()
        dish1.name = "Apple"
        dish1.price = rand1

        dish2 = MagicMock()
        dish2.name = "Banana"
        dish2.price = rand2

        order = Order()
        order.dishes = [dish1, dish2]

        order.list()
        out, err = capsys.readouterr()
        out = str(out)

        assert "Apple" in out
        assert str(rand1) in out
        assert "Banana" in out
        assert str(rand2) in out
    
    def test_total_calculates_order_total(self, capsys):
        rand1 = randint(1, 100)
        rand2 = randint(1, 100)

        dish1 = MagicMock()
        dish1.price = rand1

        dish2 = MagicMock()
        dish2.price = rand2

        order = Order()
        order.dishes = [dish1, dish2]
        order.total()

        out, err = capsys.readouterr()
        out = str(out)
        assert str(rand1 + rand2) in out
