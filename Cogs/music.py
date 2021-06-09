import discord
from discord.ext import commands
import time


class MusicCog(commands.Cog, name="music command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "music play",
					usage="",
					description = "Let HUB play the music for you !")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def play(self, ctx):
        voice_client: discord.VoiceClient = discord.utils.get(self.voice_clients, guild=guild)
        audio_source = discord.e('vuvuzela.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

def setup(bot:commands.Bot):
	bot.add_cog(MusicCog(bot))