import discord
import sys
import os 
import io
from discord.ext import commands
bot = commands.Bot(command_prefix=('!!'),description="thx for using my bot \n\nHelp Commands",owner_id=250674147980607488)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(game=discord.Game(name=f"with {len(bot.guilds)} servers!")) 
    
    
@bot.command()
async def lonely(ctx):
    await ctx.send("Ello m8! I'm online & here for you" 
                   
                   
                   
@bot.command()
async def invite(ctx):
    await ctx.send("Invite me to that server of yours: https://discordapp.com/api/oauth2/authorize?client_id=406889890970730496&permissions=0&scope=bot")
          
        
if not os.environ.get('TOKEN'):
    print("No token found!")
bot.run(os.environ.get('TOKEN').strip('"'))

    
