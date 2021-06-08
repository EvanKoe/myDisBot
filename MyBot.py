import discord
from discord import channel
from discord import guild
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
            'c_create': self.create_channel,
        }

        print('Logged on as', self.user)

    async def pong(self, ctx, msg):
        await ctx.channel.send('pong')

    async def create_channel(self, ctx, msg):
        if len(msg) != 3:
            return await ctx.channel.send('[::c_create] Create a new channel\nUSAGE: ::c_create v(ocal)/t(ext) name')
        if msg[1] == 'v' or msg[1] == 'vocal':
            #await self.guilds.create_vocal_channel(msg[2])
            await guild.create_vocal_channel(msg[2])
        elif msg[1] == 't' or msg[1] == 'text':
            #await self.guilds.create_text_channel(msg[2])
            await guild.create_text_channel(msg[2])
        print(f'Channel {msg[2]} created by {ctx.author}.')
        return await ctx.channel.send(f'Channel {msg[2]} created by {ctx.author} ! Have fun !')

    async def on_message(self, message):
        if message.author == self.user or message.author.bot:
            return
        elif not is_prefix(message.content):
            return
        else:
            tab = message.content.strip().split(' ')
            fun = self.switch.get(tab[0][2:], 'invalid')
            if fun != 'invalid':
                return await fun(message, tab)
            return await message.channel.send('Invalid command')