import asyncio
import discord
from discord.ext import commands
from cogs.functional import Functional
from cogs.messages import Messages
from cogs.poop import Poop
from cogs.fart import Fart


bot = commands.Bot(command_prefix= 'ur-anus ', intents=discord.Intents.all())

async def funccog():
    await bot.add_cog(Functional(bot))

async def messcog():
    await bot.add_cog(Messages(bot))

async def poopcog():
    await bot.add_cog(Poop(bot))

async def fartcog():
    await bot.add_cog(Fart(bot))

asyncio.run(funccog())
asyncio.run(messcog())
asyncio.run(poopcog())
asyncio.run(fartcog())

with open("token.txt") as file:
    token = file.read()

bot.run(token)