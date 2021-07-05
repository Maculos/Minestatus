from dotenv import load_dotenv
from os import environ, getenv
import discord
from discord.ext import commands

load_dotenv()
token = environ["TOKEN"]
#bot = discord.Client() 
bot = commands.Bot(command_prefix = '/') #idk how to integrate it with the / commands, to google

@bot.event
async def on_ready():
    print('Connected as {0.user}'.format(bot))

@bot.command()
async def source(ctx):
    embed=discord.Embed(title="View Source", url="https://github.com/maculos/dojacat/", description="View this project on Github.", color=discord.Color.magenta())
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('embed'):
        await source(message.channel)
    if message.content.startswith('hello'):
        await message.channel.send('Hallo!')

bot.run(token)