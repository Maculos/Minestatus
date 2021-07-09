from dotenv import load_dotenv
from os import environ, getenv
import discord
from discord.ext import commands
from random import choice
from mcstatus import MinecraftServer

load_dotenv()
token = environ["TOKEN"]
bot = commands.Bot(command_prefix = '/') #brain hort how do dat

offline_in=0
offline_msg=""
server = MinecraftServer("192.168.1.69", 25565)

@bot.event
async def on_ready():
    print('Connected as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(name="the server catch fire", type=discord.ActivityType.watching))
@bot.event
async def on_guild_join(guild):
    if guild.system_channel:
        await guild.system_channel.send(f'Hello citizens of {guild.name}!')

@bot.command(name='source', aliases=['s','src'])
async def source(ctx):
    embed=discord.Embed(title="View Source", url="https://github.com/maculos/dojacat/", description="View this project on Github.", color=discord.Color.magenta())
    await ctx.send(embed=embed)
@bot.command(name='commands', aliases=['cmds','cmd'])
async def cmd(ctx):
    embed=discord.Embed(title="Commands", url="", description="Listing all commands.", color=discord.Color.magenta())
    embed.set_thumbnail(url="https://raw.githubusercontent.com/Maculos/dojacat/main/cmd.png")
    embed.add_field(name="/source", value="Bot source code.", inline=False)
    embed.add_field(name="/commands", value="All commands", inline=False)
    embed.add_field(name="/status", value="Server status", inline=False)
    embed.add_field(name="/bind", value="Bind plugin to server", inline=False)
    embed.add_field(name="/bind channel", value="Bind all messages to channel", inline=False)
    await ctx.send(embed=embed)
@bot.command(name='shutdown', aliases=['stop'])
async def shutdown(ctx):
    embed=discord.Embed(title="Server shutdown in {0} mins".format(offline_in), url="", description=offline_msg, color=discord.Color.magenta())
    await ctx.send(embed=embed)
@bot.command()
async def online(ctx, players, ping):
    embed=discord.Embed(title="Online", url="", description="{0} players online with a ping of {1} ms".format(players, ping), color=discord.Color.green())
    await ctx.send(embed=embed)
@bot.command()
async def offline(ctx):
    embed=discord.Embed(title="Offline", url="", description="", color=discord.Color.dark_red())
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/embed') or message.content.startswith('/Embed'):
        await source(message.channel)
    if message.content.startswith('/commands') or message.content.startswith('/Commands'):
        await cmd(message.channel)
    if message.content.startswith('/status') or message.content.startswith('/Status'):
        status = server.status()
        await online(message.channel, status.players.online, status.latency)
    if message.content.startswith('/bind') or message.content.startswith('/Bind'):
        await message.add_reaction('👍')
    if message.content.startswith('/bind channel') or message.content.startswith('/Bind channel'):
        await message.add_reaction('👍')
    #tester
    if message.content.startswith('hello'):
        await message.channel.send('Hallo!')
bot.run(token)