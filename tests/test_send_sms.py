from lib.send_sms import Sms
from datetime import datetime, timedelta

class TestSms():
    def test_order_time_returns_a_time_30_minutes_ahead(self):
        sms = Sms()
        assert sms.order_time() == (datetime.now() + 
            timedelta(minutes=30)).time().strftime('%H:%M')