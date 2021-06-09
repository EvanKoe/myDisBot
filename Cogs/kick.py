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
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		# before = time.monotonic()
		# message = await ctx.send("🏓 Pong !")
		# ping = (time.monotonic() - before) * 1000
		# await message.edit(content=f"🏓 Pong !  `{int(ping)} ms`")
		await member.kick(reason=reason)
		await ctx.send(f'*Kicked {member}*')

def setup(bot:commands.Bot):
	bot.add_cog(KickCog(bot))