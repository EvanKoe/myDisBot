import discord
from discord.ext import commands
import time


class EvalCog(commands.Cog, name="eval command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name="eval",usage="",description="Your personnal calculator !")
	async def eval(self, ctx):
		try:
			expression = str(ctx.message.content.strip()[6:])
			res = eval(expression)
		except Exception as e:
			return await ctx.send('Error')
		return await ctx.send(f'*==> {res}*')
def setup(bot:commands.Bot):
	bot.add_cog(EvalCog(bot))