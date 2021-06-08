import discord
from discord import channel
from discord.message import Message
from discord.ext import commands, tasks
from random import randint

class MyBot(discord.Client):
    async def __init__(self, bot):
        self.bot = bot
        self.switch = {
            "ping": lambda: MyBot.pong,
            "create_channel": lambda: MyBot.create_channel,
        }

    async def on_ready(self):
        global status
        print('Logged on as', self.user)

    async def pong(self, message):
        await message.channel.send('pong')

    async def create_channel(self, message):
        print("You succesfully created a channel you looser")

    async def on_message(self, message):
        if message.author == self.user or message.author.bot:
            return
        self.switch.get(message)(message)

status = [
    'Epitech 2025',
    'Bot by Evan Koehler',
    'The less you sleep, the stronger you are'
]