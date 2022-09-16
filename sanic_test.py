from sanic import Sanic
from sanic.response import json, html, text
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from multiprocessing import Process,Queue,Pipe
import json

#SANIC setup
app = Sanic(__name__)
#===========
#SANIC
#==========

@app.route('/')
async def index(request):
    template = open(os.getcwd() + "/templates/index.html")
    return html(template.read())

@app.post('/spotauth')
async def spotauth(request):
    parameters = request.json
    print(parameters)
    await pipe_end.send(parameters)
    bot_return=pipe_end.recv()
    print(bot_return)
    return


def main(pipe_end):
    #pipe_end.send("hello")
    app.run(host='0.0.0.0', port=8081)
    
    

