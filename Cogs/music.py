import discord
from discord.ext import commands
import time


class MusicCog(commands.Cog, name="music command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "music play",
        usage="",
        description = "Let HUB play the music for you !"
    )
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def play(self, ctx):
		await self.bot.join_voice_channel(ctx.message.author.voice.voice_channel)
        args = ctx.message.content.split(" ")
        betterargs = " ".join(args[1:])
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=' + betterargs)
        player.start()

def setup(bot:commands.Bot):
	bot.add_cog(MusicCog(bot))