import discord
from discord.ext import commands
import time


class voiceStateCog(commands.Cog, name="voice command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "voice",
					usage="",
					description = "voice x amount of messages in chat.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def voice(self, ctx, arg, member : discord.Member):
		if arg == 'mute':
			await member.edit(mute=True)
			await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}')
		elif arg == 'deaf':
			await member.edit(deafen=True)
			await ctx.send(f'{member.mention} has been deafened by {ctx.author.mention}')
		elif arg == 'unmute':
			await member.edit(mute=False)
			await ctx.send(f'{member.mention} has been un-muted by {ctx.author.mention}')
		elif arg== 'undeaf':
			await member.edit(deafen=False)
			await ctx.send(f'{member.mention} has been un-deafened by {ctx.author.mention}')

def setup(bot:commands.Bot):
	bot.add_cog(voiceStateCog(bot))