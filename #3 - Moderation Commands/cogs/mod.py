import discord
from discord import relationship
from discord.ext import commands
from discord.ext.commands.core import command

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

#purge command
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)

#kick command
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.channel.send(f'You kicked {member.mention} for {reason}')

#ban command
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.send(f'You banned {member.mention} for {reason}')

def setup(client):
    client.add_cog(Moderation(client))
