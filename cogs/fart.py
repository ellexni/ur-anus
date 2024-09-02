import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

##play audios, links

class Fart(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fart cog successful imported!")
        print("-----------------------------")

    @commands.command(help = "prompts ur-anus to join a voice-channel")
    async def join(self, ctx):
        if (ctx.author.voice):
             if (ctx.voice_client):
              await ctx.guild.voice_client.disconnect()
             channel = ctx.message.author.voice.channel
             await channel.connect()             
        else:
             await ctx.send("i don't feel comfortable farting in open spaces...")
    
    #leave
    @commands.command(aliases = ["stop", "pause"], help= "prompts ur-anus to leave a voice-channel")
    async def leave(self, ctx):
        if (ctx.voice_client):
              await ctx.guild.voice_client.disconnect()
              await ctx.send("man all i did was fart, i couldn't poop at all")
        else:
              await ctx.send("i'm not in the washroom yet...")

    @commands.command(help = "produces vine boom audios")
    async def fart_boom(self, ctx):
        source = FFmpegPCMAudio('boom.mp3')
        if (ctx.author.voice):
              if (ctx.voice_client):
                   await ctx.guild.voice_client.disconnect()
              channel = ctx.message.author.voice.channel
              voice = await channel.connect()
              player = voice.play(source)
              self.is_playing = True
        else:
             await ctx.send("i'm not in the washroom yet...")

    @commands.command(help = "produces 'happy happy happy' cat audio")
    async def fart_happy(self, ctx):
        source = FFmpegPCMAudio('happy.mp3')
        if (ctx.author.voice):
              if (ctx.voice_client):
                   await ctx.guild.voice_client.disconnect()
              channel = ctx.message.author.voice.channel
              voice = await channel.connect()
              player = voice.play(source) 
              self.is_playing = True 
        else:
             await ctx.send("i'm not in the washroom yet...")