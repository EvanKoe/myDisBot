import discord
from discord.ext import commands
import time


class KickCog(commands.Cog, name="kick command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "kick",
					usage="",
					description = "Kick member from server.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member:discord.Member=None, *, reason=None):
		if member == None:
			return await ctx.send('*I should have kicked you, traitor !\nUSAGE:\n\t::kick mention#0000*')
		if reason == None:
			reason = "You were bad"
		await member.kick(reason=reason)
		return await ctx.send(f'*{member.mention} kicked by {ctx.message.author.mention}*')

def setup(bot:commands.Bot):
	bot.add_cog(KickCog(bot))