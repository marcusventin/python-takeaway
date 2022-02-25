from unittest.mock import MagicMock, patch
from random import randint

from lib.order import Order
from lib.send_sms import Sms


class TestOrder():
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

    @patch.object(Sms, 'send')
    def test_confirm_sends_sms(self, mocked_sms):
        order = Order()
        order.confirm()
        mocked_sms.assert_called()
