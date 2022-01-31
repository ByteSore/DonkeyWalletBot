import discord
from discord.ext import tasks, commands
from pprint import pprint
import psql
import logging
import botCog

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

#guildIDs = [157206684844949504, 932672283321966602]

initial_extensions = ['cogs.find']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="DonkeTunes"))
    print(f'Successfully logged in and booted...!')

bot.run("OTM3Mjg3ODEwMzkyNjc0MzA1.YfZjSw.1h4pzeJV6kyO8pJ2GKfvBOU44Zw")


