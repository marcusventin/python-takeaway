from twilio.rest import Client
from datetime import datetime, timedelta
from dotenv import load_dotenv, dotenv_values

load_dotenv()
env_values = dotenv_values(".env")

class Sms():
    def __init__(self):
        # Your Account SID from twilio.com/console
        self.account_sid = env_values["ACCOUNT_SID"]
        # Your Auth Token from twilio.com/console
        self.auth_token  = env_values["AUTH_TOKEN"]

    def send(self):
        client = Client(self.account_sid, self.auth_token)
        time = self.order_time()
        message = client.messages.create(
            to=env_values["TO"], 
            from_=env_values["FROM"],
            body="Thank you! Your order was placed and will be delivered "
                f"before {time}")

        print(message.sid)
    
    def order_time(self):
        order_time = (datetime.now() + timedelta(minutes=30)).time()
        return(order_time.strftime('%H:%M'))