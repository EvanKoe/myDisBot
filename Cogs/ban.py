import discord
from discord.ext import commands
import time


class BanCog(commands.Cog, name="ban command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "ban",
					usage="",
					description = "Ban member from server.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member:discord.Member=None, *, reason=None):
		if member == None:
			return await ctx.send('*You want me to ban someone randomly, don\'t you ?\nUSAGE:\n\t::ban user#0000*')
		await member.ban(reason=reason)
		await ctx.send(f'*{member} banned by {ctx.message.author}*')
		return print(f'*{member} banned by {ctx.message.author}*')

def setup(bot:commands.Bot):
	bot.add_cog(BanCog(bot))