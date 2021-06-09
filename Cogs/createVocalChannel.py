import discord
from discord import guild, channel
from discord.ext import commands
import time


class VocalCreateCog(commands.Cog, name="createVocal command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "createVocal",
					usage="",
					description = '''Create a new vocal channel.
					**Parameters: **
					<channel name> : name of your channel''',
					aliases=['cv'])
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def createVocal(self, ctx, channel_name=None, cat_name:str=None):
		if channel_name != None:
			channel_name = channel_name.replace('-', ' ')
		else:
			return await ctx.send(f'*USAGE (because {ctx.author.mention} didn\'t understand):\n\t::createVocal name-of-your-channel*')
		if cat_name != None:
			cat_name = cat_name.upper()
		category = discord.utils.get(ctx.guild.categories, name=cat_name)
		await ctx.guild.create_voice_channel(name=channel_name, category=category)
		return await ctx.send(f'*Channel {channel_name} created by {ctx.author.mention}! Enjoy!*')

def setup(bot:commands.Bot):
	bot.add_cog(VocalCreateCog(bot))