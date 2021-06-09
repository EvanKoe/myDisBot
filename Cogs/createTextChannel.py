import discord
from discord import guild, channel
from discord.ext import commands
import time


class TextCreateCog(commands.Cog, name="createText command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "createText",
					usage="",
					description = '''Create a new text channel.
					**Parameters: **
					<channel name> : name of the text channl
					<category name> : category you want your channel to be in''',
					aliases=['ct'])
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def createText(self, ctx, channel_name:str, name:str):
		name = name.replace('-', ' ')
		channel_name = channel_name.replace('-', ' ')
		category = discord.utils.get(ctx.guild.categories, name=name)
		await ctx.guild.create_text_channel(name=channel_name,  category=category)
		await ctx.send(f'*Channel {channel_name} created by {ctx.author.mention}! Enjoy!*')

def setup(bot:commands.Bot):
	bot.add_cog(TextCreateCog(bot))