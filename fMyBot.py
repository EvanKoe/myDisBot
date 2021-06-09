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
            'help': self.get_help,
            'c_create': self.create_channel,
            'c_clear': self.clear_channel,
            'u_ban': self.ban_user,
            'm_play': self.play_music
        }

        print('Logged on as', self.user)

    async def pong(self, ctx, msg):
        await ctx.channel.send('pong')

    async def get_help(self, ctx, msg):
        await ctx.channel.send('Hi ! I\'m HUB, a little Discord bot !\n')
        await ctx.channel.send('Here are a bunch of commands you can send me !\n')
        for key in self.switch:
            await ctx.channel.send(key)
        return

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
        if len(msg) > 1:
            limit = int(msg[1])
        await ctx.channel.purge(limit=limit)
        print(f'@{ctx.author} cleared the chat !')
        return await ctx.channel.send('Well, you\'ve got a nice clean chat now !')

    async def ban_user(self, ctx, msg):
        reason = None
        if len(msg) == 1:
            return await ctx.channel.send('Who\'s the poor guy you wanna ban ?\nUSAGE\n\t::u_ban @Name#xxxx')
        if len(msg) == 3:
            reason = msg[2]
        user = await self.fetch_user(msg[1])
        await user.ban(reason = reason)
        return await ctx.channel.send(f'The poor @{msg[1]} has been banned. Do your bereavement, now...')

    async def play_music(self, ctx, msg):
        if ctx.author.voice.voice_channel == None:
            return ctx.channel.send('Where do I have to play the music ? Join a vocal channel first !')
        voice = await self.join_voice_channel(ctx.author.voice.voice_channel)
        if "http" in msg[1]:
            player = await voice.create_ytdl_player(msg[1])
        else:
            player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=' + msg[1])
        player.start()

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
            return await message.channel.send('Invalid command. Type ::help to get help !')