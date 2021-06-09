import discord
from discord.ext import commands
import time


class TemplateCog(commands.Cog, name="template command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "template",
					usage="",
					description = "Creates a new template for the server.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def template(self, ctx, name):
		await ctx.guild.create_template(name=name, description=None)
		await ctx.send(f'{ctx.author.mention} has created a new template named {name}')

def setup(bot:commands.Bot):
	bot.add_cog(TemplateCog(bot))