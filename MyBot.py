import discord
from discord import channel
from discord.abc import _Undefined
from discord.message import Message
from discord.ext import commands, tasks
from random import randint

def is_prefix(msg):
    if msg[:2] == '::':
        return True
    return False

class MyBot(discord.Client):
    async def on_ready(self):
        self.status = [
        'Epitech 2025',
        'Bot by Evan Koehler',
        'The less you sleep, the stronger you are'
        ]
        self.switch = {
            'ping': self.pong,
            'create_channel': self.create_channel,
        }
        print('Logged on as', self.user)

    async def pong(self, message):
        await message.channel.send('pong')

    async def create_channel(self, message):
        message.content
        print(f'Channel created.')
        await message.channel.send('create_channel')

    async def on_message(self, message):
        if message.author == self.user or message.author.bot:
            return
        elif not is_prefix(message.content):
            return
        fun = self.switch.get(message.content[2:], 'invalid')
        if fun != 'invalid':
            return await fun(message)
        return