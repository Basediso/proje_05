import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptık")

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord genel haber botuyum!')

@bot.command()
async def ntv_link(ctx):
    await ctx.send("https://www.ntv.com.tr/")

@bot.command()
async def tv100_link(ctx):
    await ctx.send("https://www.tv100.com/")

@bot.command()
async def now_link(ctx):
    await ctx.send("https://www.nowtv.com.tr/")

@bot.command()
async def cnnturk_link(ctx):
    await ctx.send("https://www.cnnturk.com/")

@bot.command()
async def bbc_link(ctx):
    await ctx.send("https://www.bbc.com/")

@bot.command()
async def yt_link(ctx):
    await ctx.send("https://www.youtube.com/?app=desktop&hl=tr")

bot.run("TOKEN!")
