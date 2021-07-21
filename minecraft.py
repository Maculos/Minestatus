# https://github.com/maculos/MineStatus/

import os, sys
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

# Extra Imports
from mcstatus import MinecraftServer
from discord import Embed, Color
server = MinecraftServer("192.168.1.69", 25565)

class MineStatus(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="status", help="Gets the server's status.")
	async def status(self, ctx):
		try:
			status = server.status()
			embed=Embed(title="Online", url="", description="{0} players online with a ping of {1} ms".format(status.players.online, status.latentcy), color=Color.green())
			await ctx.send(embed=embed)
		except:
			embed=Embed(title="Offline", url="", description="", color=Color.dark_red())
			await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(MineStatus(bot))

if __name__ == "__main__":
	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	import prism
	prism.main()