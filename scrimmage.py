import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    cmds = message.content.split()
    # So that we don't interfere with other messages.
    if cmds[0] != "!scr":
        return
    
    if "Hello" in message.content:
        await message.channel.send("Hello there")

client.run(TOKEN)