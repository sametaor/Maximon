
#importing modules
import discord
import discord.ext.tasks as tasks
import logging

#Intents for bot
intents = discord.Intents.all()
intents.message_content = True

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
    
    status = (['Python','Git','Github','VSCode','Windows','Discord.py'])
    @tasks.loop(seconds=30)
    async def status_swap():
        await maxi.change_presence(activity=discord.Game(next(status)))
        

#Preparing client to run
client = Maximon(intents=intents)
client.run('MTIwMzcyNzA1NTAwNzUxNDYzNA.G-zEUn.7sZARtd18HMQ0gXmLaDVP4mQvbDsto5-rVKzpc')