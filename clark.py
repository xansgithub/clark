# bot.py
import os

import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = "OTUwOTc4OTc4NDg1NzY0MTA2.YigyMA.qbF4RJ8uOX5Z0uwsKGgcbkpUOfo"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'farting':
        await message.channel.send("i farted lol")

client.run(TOKEN)