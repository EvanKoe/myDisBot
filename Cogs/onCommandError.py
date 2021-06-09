import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
import time


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				await ctx.send('This command has a cooldown, be sure to wait for '+str(day)+ "day(s)")
			elif hour > 0:
				await ctx.send('This command has a cooldown, be sure to wait for '+str(hour)+ " hour(s)")
			elif minute > 0:
				await ctx.send('This command has a cooldown, be sure to wait for '+ str(minute)+" minute(s)")
			else:
				await ctx.send(f'This command has a cooldown, be sure to wait for {error.retry_after:.2f} second(s)')
		elif isinstance(error, CommandNotFound):
			await ctx.send('*Error: Command Not Found*')
			return
		elif isinstance(error, MissingPermissions):
 			#await ctx.send(error.text)
			await ctx.send('*Error: Missing Permissions*')
		elif isinstance(error, CheckFailure):
			#await ctx.send(error.original.text)
			await ctx.send('*Error: Check Failure*')
		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('*Error: Missing Argument*')
		else:
			print(error)

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))