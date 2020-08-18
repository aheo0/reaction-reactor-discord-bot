import discord

from bot import *
from commands import *
from database import *
from embeds import *

client = discord.Client()

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    content = message.content
    if (message.content.startswith("/add ")):
        await AddReaction(message).run()

client.run(DISCORD_TOKEN)