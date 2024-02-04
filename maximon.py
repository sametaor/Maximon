
#importing modules
import discord
import discord.ext.tasks as tasks
import logging
from dotenv import load_dotenv
import os

#Intents for bot
intents = discord.Intents.all()
intents.message_content = True

load_dotenv('token.env')

#Bot class
class Maximon(discord.Client):
    maxi = discord.Client(intents=intents)
    
    #Logging bot in
    @maxi.event
    async def on_ready(self):
        print(f'{self.user} is online!')
    
    #Resolving self replies
    @maxi.event
    async def on_message(message):
        if message.author == maxi.user:
            return
        

#Preparing client to run
client = Maximon(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
