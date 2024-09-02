import discord
from discord.ext import commands
import os
import random

class Poop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Poop cog successful imported!")
        print("---------------------------------")

    @commands.command(aliases = ["poop_wtf", "poop_what"], help = "produces a random :| photo")
    async def poop_bruh(self, ctx):
         urls = []
         fin = open('bruh_poop.txt')
         url = fin.readline()
         while url != "":
             urls.append(url.strip())
             url = fin.readline()
         selected_file = random.choice(urls)
         embedded_msg = discord.Embed(title= "bruh", color= discord.Color.random())
         embedded_msg.set_image(url = selected_file) #the meme
         embedded_msg.set_footer(text= f"sent from {ctx.author}", icon_url = ctx.author.avatar)
         await ctx.send(embed = embedded_msg)
         
    @commands.command(aliases = ["poop_side", "poop_sideeye", "poop_mhm"], help = "produces a side eye photo") #doesnt work with the space?
    async def poop_bombastic(self, ctx):
         urls = []
         fin = open('bombastic_poop.txt')
         url = fin.readline()
         while url != "":
             urls.append(url.strip())
             url = fin.readline()
         selected_file = random.choice(urls)
         embedded_msg = discord.Embed(title= "bombastic side eye", color = discord.Color.random())
         embedded_msg.set_image(url= selected_file)
         embedded_msg.set_footer(text = f"sent fromt {ctx.author}", icon_url = ctx.author.avatar)
         await ctx.send(embed = embedded_msg)
