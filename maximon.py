
#importing modules
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
from itertools import cycle
import os

#Intents for bot
intents = discord.Intents.all()
intents.message_content = True

load_dotenv('token.env')

maxi = discord.ext.commands.Bot(command_prefix='&', intents=intents)

status=cycle(["Git","Github","Discord","Discord.py","Python"])

@tasks.loop(seconds=60)
async def status_swap():
    await maxi.change_presence(activity=discord.Game(next(status)))
#Bot class
@maxi.event
async def on_ready():
        print(f'{maxi.user} is online!')
        status_swap.start()
    
#Resolving self replies
@maxi.event
async def on_message(message):
        if message.author == maxi.user:
            return

#Preparing client to run
maxi.run(os.getenv("DISCORD_TOKEN"))
