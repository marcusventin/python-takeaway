from lib.menu import Menu
from lib.send_sms import Sms

class Order(Menu):
    def __init__(self):
        super().__init__()
        self.sms = Sms()
    
    def summary(self):
        self.list()
        self.total()

    def total(self):
        total = sum([dish.price for dish in self.dishes])
        print("Total: £", total)

    def confirm(self):
        self.sms.send()

