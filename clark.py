# bot.py
import os

import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = ""

client = discord.Client()

friends = ['yvonne', 'devin', 'alex', 'farley', 'stu', 'stuart', 'kyle', 'tanner', 'steve', 'johnny', 'memi', 'emily', 'winston', 'maddie', 'jake', 'val', 'valiant']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'farting' in message.content:
        await message.channel.send("i farted lol")
    for friend in friends:
        if friend in message.content:
            await message.channel.send(friend.upper() + " FARTED!!!")

client.run(TOKEN)