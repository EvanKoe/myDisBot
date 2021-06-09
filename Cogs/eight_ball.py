import discord
from discord.ext import commands
import time
import random


class _8ballCog(commands.Cog, name="_8ball command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name="_8ball",usage="",description="Insult member from server.",aliases=['8ball'])
	async def _8ball(self, ctx, *, question):
		responses = [
            'Elephant.'
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]
		await ctx.channel.purge(limit=1)
		return await ctx.send(
			f'({ctx.author.mention}) **Question:** {question}\n**Answer:** {random.choice(responses)}'
        )

def setup(bot:commands.Bot):
	bot.add_cog(_8ballCog(bot))