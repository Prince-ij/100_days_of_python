from twitterbot import InternetSpeedTwitterBot
from config import *
bot = InternetSpeedTwitterBot()

up, down = bot.get_internet_speed()

if up < PROMISED_UP or down < PROMISED_DOWN:
    msg = f"Hey, why did I get {up}/{down} Internet speed instead of {PROMISED_UP}/{PROMISED_UP} you promised !"
    bot.tweet_at_provider(msg)
