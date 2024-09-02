import discord
from discord.ext import commands

class Functional(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("The bot is ready for use!")
        print("-------------------------")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
         print("The bot has joined a new guild!")
         print("-----------------------------")
         welcome = open("welcome.txt")
         text = welcome.read()
         channel = guild.system_channel
         await channel.send(text)

    