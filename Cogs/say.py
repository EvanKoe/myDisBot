import discord
from discord.ext import commands
import time


class SayCog(commands.Cog, name="say command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name="say",usage="",description="Want me to say something ?")
	async def say(self, ctx, *, msg:str=None):
		if msg == None:
			return await ctx.send('If you have nothing to say, just be quiet.')
		await ctx.channel.purge(limit=1)
		return await ctx.channel.send(msg)
def setup(bot:commands.Bot):
	bot.add_cog(SayCog(bot))