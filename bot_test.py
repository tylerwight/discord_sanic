from sanic import Sanic
from sanic.response import json, html, text
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

#DISCORD setup
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="^",intents=intents)



#=========
#BOT COMMANDS
#=========

@bot.command(brief="test ping pong command")
async def ping(ctx):
    await ctx.send("bitch")




def main(pipe_end):
    #a = pipe_end.recv()
    #print(a)

    bot.run(TOKEN)


