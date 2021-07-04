from dotenv import load_dotenv
from os import environ, getenv
import discord
from discord.ext import commands

load_dotenv()
token = environ["TOKEN"]
#bot = discord.Client()
bot = commands.Bot(command_prefix = '!')

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('embed'):
        await embed(message.channel)
    if message.content.startswith('hello'):
        await message.channel.send('Hallo!')

bot.run(token, bot=True, reconnect=False)