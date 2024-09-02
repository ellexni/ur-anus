import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Messages cog successful imported!")
        print("---------------------------------")

    @commands.command(aliases = ["hi", "yo", "whaddup"], help="prompts ur-anus to give a cute little message to you!")
    async def hello(self, ctx):
         await ctx.send(f"where's the washroom {ctx.author.mention}? i'm feeling gassy!")