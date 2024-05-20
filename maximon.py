
#importing modules
import discord
import os
import dotenv as de
from discord.ext import tasks, commands
from itertools import cycle

#opening env file
de.load_dotenv("token.env")

tokenbool=input(str("Would you like to add/edit your bot token?(y/n|default:n)"))
if tokenbool == "y":
    # taking input of discord bot token from user
    token=input(str("Enter your bot token: "))

    # looking for DISCORD_TOKEN variable in env file and editing it if there is an entry already, and adding the input string as new variable DISCORD_TOKEN, if empty
    if os.getenv("DISCORD_TOKEN") is None:
        os.environ["DISCORD_TOKEN"]=token
        de.set_key("token.env","DISCORD_TOKEN", os.environ["DISCORD_TOKEN"])
        print("Token added!")
    elif os.getenv("DISCORD_TOKEN") is not None:
        de.load_dotenv("token.env", override=True)
        os.environ["DISCORD_TOKEN"] = token
        de.set_key("token.env", "DISCORD_TOKEN", os.environ["DISCORD_TOKEN"], quote_mode='never')
        print("Token updated!")

elif tokenbool == None or tokenbool == "n":
    print("Please verify that you have a DISCORD_TOKEN variable in the token.env file, otherwise the bot will throw errors.")

#Intents for bot
intents = discord.Intents.all()
intents.message_content = True

de.load_dotenv('token.env')

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
