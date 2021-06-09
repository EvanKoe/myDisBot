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
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		# before = time.monotonic()
		# message = await ctx.send("🏓 Pong !")
		# ping = (time.monotonic() - before) * 1000
		# await message.edit(content=f"🏓 Pong !  `{int(ping)} ms`")
		await member.ban(reason=reason)
		await ctx.send(f'*Banned {member}*')

def setup(bot:commands.Bot):
	bot.add_cog(BanCog(bot))