import time
import json
from discord.ext import commands
from colorama import Fore
import sys
import discord
import os
# ---------------------------------------- Imports
config = json.load(open('config.json', 'rb'))

########### >> Defining
os.system("color")

########### >> typing print define

def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0000000000000000000000001)

########### >> Classes
class Colours:
    White = "\x1b[38;2;250;250;250m"
    Magenta = "\x1b[38;2;255;94;255m"

########### >> important shit

prefix = config['prefix']
version = "1.0"
bot = commands.Bot(command_prefix=prefix, self_bot=True)

########### >> loading stuff
def new_splash():
    typingprint(f"Loaded the bot prefix is {Fore.Magenta}+{config['prefix']}+{Fore.RESET}")


def Clear():
    os.system('cls')

########### >> cmds below

typingprint(f"Loaded the bot prefix is {config['prefix']}")

url1 = "https://www.twitch.tv/monstercat"

@bot.command()
async def stream(ctx, *, cum):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=cum,
        url=url1, 
    )
    msg = f"""
```ini
[Stream]
Set your streaming to [{cum}]
```
    """
    await bot.change_presence(activity=stream)
    await ctx.send(msg,delete_after = 30)    

@bot.command()
async def game(ctx, *, cum):
    await ctx.message.delete()
    game = discord.Game(
        name=cum,
    )
    msg = f"""
```ini
[game]
Set your Game to [{cum}]
```
    """
    await bot.change_presence(activity=game)
    await ctx.send(msg,delete_after = 30)

@bot.command()
async def listening(ctx, *, cum):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=cum,
        )) 
    msg = f"""
```ini
[listening]
Set your listening to [{cum}]
```
    """
    await ctx.send(msg,delete_after = 30)      

@bot.command()
async def watching(ctx, *, cum):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=cum,
        )) 
    msg = f"""
```ini
[watching]
Set your watching to [{cum}]
```
    """
    await ctx.send(msg,delete_after = 30)

def Init():
    with open('config.json', encoding="utf-8") as f:
        config = json.load(f)
    token = config.get('token')
    try:
        bot.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        input(f"{Fore.RED}[SYSTEM] TOKEN IS INVALID CHECK CONFIG"+Colours.White)
        sys.exit
        python = sys.executable
        os.execl(python, python, * sys.argv)
Init()