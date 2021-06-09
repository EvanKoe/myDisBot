import discord
from discord import guild, channel
from discord.ext import commands
import time


class CategoryCreateCog(commands.Cog, name="createCategory command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	@commands.command(name = "createCategory",
					usage="",
					description = '''Create a new category.
					**Parameters: **
					<category name> : name of the category''',
					aliases=['cc'])
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def createCategory(self, ctx, cat_name:str):
		cat_name = cat_name.replace('-', ' ')
		await ctx.guild.create_category(name=cat_name)
		await ctx.send(f'*Category {cat_name} created by {ctx.author.mention}! Enjoy!*')

def setup(bot:commands.Bot):
	bot.add_cog(CategoryCreateCog(bot))