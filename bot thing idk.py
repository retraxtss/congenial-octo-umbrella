import asyncio
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="1")

@bot.event
async def on_ready() :
    print("Connected and ready to use")

@bot.command(pass_context=True)
async def ping(ctx):
        mapChoice = ""
        rng = random.randint(0, 140)
        if rng <= 20:
            mapChoice = "Customs"
        elif rng <= 40:
            mapChoice = "Reserve"
        elif rng <= 60:
            mapChoice = "Labs"
        elif rng <= 80:
            mapChoice = "Interchange"
        elif rng <= 100:
            mapChoice = "Shoreline"
        elif rng <= 120:
            mapChoice = "Woods"
        elif rng <= 140:
            mapChoice = "Factory"
        await ctx.send(mapChoice)

bot.run("Njc5MTcwNDczODQ1NTg3OTc4.XktdBw.-DVGxk1Bh6TaHkH8OLPv0JHCvAA")