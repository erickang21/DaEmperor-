imports
import discord
import sys
import os 
import io
from discord.ext import commands
bot = commands.Bot(command_prefix=('!!'),description="your dream bot \n\nHelp Commands",owner_id=[250674147980607488])


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(game=discord.Game(name=f"with {len(bot.guilds)} servers!")) 
    
    
@bot.command
async def test(ctx):
    await ctx.send("Online.")
    
    
if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))   
