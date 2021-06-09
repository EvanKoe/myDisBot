import discord
from discord.ext import commands
import time


class EasterEggCog(commands.Cog, name="hello_there command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name="hello_there",usage="",description="Only chosen ones got that...")
	async def helloThere(self, ctx):
		return await ctx.channel.send(file=discord.File('src/general_kenobi.gif'))

	@commands.command(name="archi",usage="",description="You are not Archi")
	async def archi(self, ctx):
		return await ctx.channel.send(file=discord.File('src/man_of_culture.jpg'))

	@commands.command(name="wednesday",usage="",description="Frog lover")
	async def frog(self, ctx):
		return await ctx.channel.send(file=discord.File('src/frog.jpg'))

	@commands.command(name="aer",usage="",description="You are not alone")
	async def aer(self, ctx):
		await ctx.channel.send('Our pedagogical team has been notified (I\'m joking, look on the Internet)')
		return await ctx.channel.send(file=discord.File('src/bad.png'))

def setup(bot:commands.Bot):
	bot.add_cog(EasterEggCog(bot))