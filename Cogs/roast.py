import discord
from discord.ext import commands
import time
import random


class roastCog(commands.Cog, name="roast command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name="flirt",usage="",description="Flirt with a member of your choice")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def roast(self, ctx, member: discord.Member):
		await ctx.channel.purge(limit=1)
		roast = [
			'You are more disappointing than an unsalted pretzel.',
			'Light travels faster than sound, which is why you seemed bright until you spoke.',
			'We were happily married for one month, but unfortunately, we’ve been married for 10 years.',
			'You\'re so annoying you could make your Happy Meal cry.',
			'You have so many gaps in your teeth it looks like your tongue is in jail.',
			'Your secrets are always safe with me. I never even listen when you tell me them.',
			'Hold still. I’m trying to imagine you with a personality.',
			'Your face makes onions cry.',
			'I’m not insulting you; I’m describing you.',
			'I’m not a nerd; I’m just smarter than you.',
			'Don’t be ashamed of who you are. That’s your parents’ job.',
			'Your face is just fine, but we’ll have to put a bag over that personality.',
			'You bring everyone so much joy… when you leave the room.',
			'I thought of you today. It reminded me to take out the trash.',
			'Don’t worry about me. Worry about your eyebrows.',
			'If you’re going to be two-faced, at least make one of them pretty.',
			'You are like a cloud. When you disappear, it’s a beautiful day.',
			'I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?',
			'Is your ass jealous of the amount of shit that comes out of your mouth?',
			'If I throw a stick, will you leave?'
		]
		return await ctx.send(f'{member.mention} {random.choice(roast)}')

def setup(bot:commands.Bot):
	bot.add_cog(roastCog(bot))