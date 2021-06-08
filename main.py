import discord
from MyBot import MyBot
import os

case_insensitive = True

bot = MyBot()
bot.run(os.environ.get('SECRET'))