import discord
from discord.ext import commands, tasks
import json
import os
from dotenv import load_dotenv
from itertools import cycle

# Get configuration .env
load_dotenv('.env')
token = os.getenv('SECRET')
prefix = os.getenv('PREFIX')

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print('Discord.py version : ', discord.__version__)
	activity_watching = discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help")
	status_invisible = discord.Status.invisible
	status_online = discord.Status.online
	status_idle = discord.Status.idle
	status_dnd = discord.Status.do_not_disturb
	await bot.change_presence(status = status_dnd, activity=activity_watching)

bot.run(token)