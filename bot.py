import discord, os

try:
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
except:
    with open("local_auth/bot_token.txt") as f:
        DISCORD_TOKEN = f.read()