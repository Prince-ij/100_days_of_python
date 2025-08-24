from data import Data
import yagmail
from config import YAGMAIL_KEY

class Notify:
    def __init__(self):
        self.data = Data()
        self.messages = self.data.get_lowest_price()

        self.emails = self.data.get_emails() # get all emails from the sheet
        for message in self.messages:
             yag = yagmail.SMTP("baaby.dudu@gmail.com", YAGMAIL_KEY)
             for email in self.emails:
                yag.send(email, "Cheap Flight", message)
             print(message)
