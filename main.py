import discord
import os
from discord import client
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print("Bot is Online!")

client.run(TOKEN)