imports
import discord
import sys
import os 
import io
from discord.ext import commands
bot = commands.Bot(command_prefix=('[!!]'),description="[your dream bot] \n\nHelp Commands",owner_id=[250674147980607488])
@bot.command()
async def commandname(ctx):
    code goes here
    await ctx.send("msg does here")
    if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!!'),description="Short bot description\n\nHelp Commands",owner_id=250674147980607488)
    
