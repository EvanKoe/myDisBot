import discord
from discord.ext import commands
import time

class ClearCog(commands.Cog, name="clear command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "clear",
					usage="",
					description = "clear x amount of messages in chat.",
					aliases = ['cls'])
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def clear(self, ctx, amount=100):
		amount = amount + 1
		if amount > 100:
			amount = 101
			await ctx.send(f'Warning ! You cannot delete more than 100 messages !')
		await ctx.channel.purge(limit=amount)
		return print(f'{amount - 1} messages have been purged in {ctx.channel.mention}')

def setup(bot:commands.Bot):
	bot.add_cog(ClearCog(bot))