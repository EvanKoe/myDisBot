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
            'c_clear': self.clear_channel
        }

        print('Logged on as', self.user)

    async def pong(self, ctx, msg):
        await ctx.channel.send('pong')

    async def create_channel(self, ctx, msg):
        if len(msg) != 3:
            return await ctx.channel.send('[c_create] Create a new channel\n\nUSAGE:\n\t::c_create v(ocal)/t(ext) name')
        msg[1] = msg[1].lower()
        if msg[1] == 'v' or msg[1] == 'vocal':
            await ctx.guild.create_voice_channel(name=msg[2])
        elif msg[1] == 't' or msg[1] == 'text':
            await ctx.guild.create_text_channel(name=msg[2])
        print(f'Channel {msg[2]} created by @{ctx.author}.')
        return await ctx.channel.send(f'Channel {msg[2]} created by @{ctx.author} ! Have fun !')

    async def clear_channel(self, ctx, msg):
        limit = 100
        if (len(msg) > 1):
            limit = int(msg[1])
        await ctx.channel.purge(limit=limit)
        print(f'@{ctx.author} cleared the chat !')
        return await ctx.channel.send('Well, you\'ve got a nice clean chat now !')

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