from unittest.mock import MagicMock

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
    
    def test_view_shows_list_of_items(self):
        dish1 = MagicMock()
        dish1.name = "Apple"
        dish1.price = 2

        dish2 = MagicMock()
        dish2.name = "Banana"
        dish2.price = 3

        order = Order()
        order.dishes = [dish1, dish2]

        list = order.view()

        assert "Apple" in list[0]
        assert "£2" in list[0]
        assert "Banana" in list[1]
        assert "£3" in list[1]