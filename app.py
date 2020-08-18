import discord

from bot import *
from database import *
from embeds import *

client = discord.Client()

@client.event
async def on_ready():
    print("Ready")

client.run(DISCORD_TOKEN)