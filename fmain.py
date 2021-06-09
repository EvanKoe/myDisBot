import discord
from MyBot import MyBot
from dotenv import load_dotenv
import os

load_dotenv('.env')
case_insensitive = True

bot = MyBot()
bot.run(os.getenv('SECRET'))