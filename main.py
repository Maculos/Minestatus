from dotenv import load_dotenv
from os import environ, getenv
import discord
from discord.ext import commands
from random import choice

load_dotenv()
token = environ["TOKEN"]
bot = commands.Bot(command_prefix = '/') #idk how to integrate it with the / commands, to google

@bot.event
async def on_ready():
    print('Connected as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(name="the server catch fire", type=discord.ActivityType.watching))

@bot.command()
async def source(ctx):
    embed=discord.Embed(title="View Source", url="https://github.com/maculos/dojacat/", description="View this project on Github.", color=discord.Color.magenta())
    await ctx.send(embed=embed)
@bot.command()
async def cmd(ctx):
    embed=discord.Embed(title="Commands", url="", description="Listing all commands.", color=discord.Color.magenta())
    embed.set_thumbnail(url="https://raw.githubusercontent.com/Maculos/dojacat/main/cmd.png")
    embed.add_field(name="/source", value="Link to bot source code.", inline=False)
    embed.add_field(name="/commands", value="All commands", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/embed') or message.content.startswith('/Embed'):
        await source(message.channel)
    if message.content.startswith('/commands') or message.content.startswith('/Commands'):
        await cmd(message.channel)
    #tester
    if message.content.startswith('hello'):
        await message.channel.send('Hallo!')
bot.run(token)