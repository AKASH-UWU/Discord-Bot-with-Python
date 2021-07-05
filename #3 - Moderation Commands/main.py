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

##member event
@client.event 
async def on_member_join(member):
    if member.guild.name == "Your_Server_Name":
        embed = discord.Embed(description=f'Hey {member.mention}, Welcome to **{member.guild.name}**',
                                colour=discord.Colour.red())
        await client.get_channel(854624186118438933).send(embed=embed)
        role = discord.utils.get(member.guild.roles, name='Role_Name')
        await member.add_roles(role)

##Cogs loader
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

for filenames in os.listdir('./cogs'):
    client.load_extension(f'cogs.{filenames[:-3]}')       

@client.event
async def on_ready():
    print("Bot is Online!")

client.run(TOKEN)
