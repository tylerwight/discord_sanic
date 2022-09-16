from sanic import Sanic
from sanic.response import json, html, text
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from multiprocessing import Process,Queue,Pipe


#SANIC setup
app = Sanic(__name__)
#===========
#SANIC
#==========
@app.route('/')
async def index(request):
    template = open(os.getcwd() + "/templates/index.html")
    return html(template.read())



def main(pipe_end):
    app.run(host='0.0.0.0', port=8081)
    pass

