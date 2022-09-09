import discord
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

from discord.ext import commands

client = discord.client()
bot = commands.Bot(command_prefix="e!")

@client.event
async def on_ready():
    print("Logged on as {0.user}".format(client))

@client.event
async def on_message(message):
    message.content = message.content.lower().replace(" ", "")

    if message.author == client.user:
        return
    
    if message.content.startswith("e!help"):
        await message.channel.send("This is a help menu without any embeds because I have not added any as of yet.")

    if message.content.startswith("e!twitter"):
        await message.channel.send("https://www.twitter.com/excane")

    if message.content.startswith("e!twitch"):
        await message.channel.send("https://www.twitch.tv/zentriex")

    if message.content.startswith("e!owners"):
        await message.channel.send("Zentriex and Zylen")

    if message.content.startswith("e!cc"):
        await message.channel.send("Sinnn, ")

client.run(os.getenv("DISCORD_TOKEN"))