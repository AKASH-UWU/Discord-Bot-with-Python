import discord
import os
from discord import client
from dotenv import load_dotenv
from discord.ext import commands
from discord import guild


client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event 
async def on_member_join(member):
    if member.guild.name == "Server_Name":
        embed = discord.Embed(description=f'Hey {member.mention}, Welcome to **{member.guild.name}**',
                                colour=discord.Colour.red())
        await client.get_channel(854624186118438933).send(embed=embed)
        role = discord.utils.get(member.guild.roles, name='ROLE_NAME')
        await member.add_roles(role)

@client.event
async def on_ready():
    print("Bot is Online!")

client.run(TOKEN)
