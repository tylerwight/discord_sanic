from sanic import Sanic
from sanic.response import json, html, text
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import asyncio
import spotipy
import spotipy.util as util
from spotipy import oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import CacheFileHandler
import time


loop = asyncio.get_event_loop()


#DISCORD setup
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="^",intents=intents)

#SANIC setup
app = Sanic(__name__)

#SPOTIFY setup
scope = 'playlist-modify-public'
cache_path = "./.cachehere"
spotify_connections = []
cid = os.getenv('SPOTIPY_CLIENT_ID')
secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_url = "http://10.100.1.90:8081"
sp_oauth = oauth2.SpotifyOAuth( cid, secret, redirect_url,scope=scope,cache_path=cache_path)

#username = os.getenv('SPOTIPY_USERNAME')
#scope = 'playlist-modify-public'
#cache_path = "./cachehere"
#handler = CacheFileHandler(cache_path=cache_path, username=username)
#spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri="http://localhost:8080", scope=scope, cache_handler=handler, open_browser=False))
#print(spotify)
#print(spotify.user_playlists(username))

#=========
#BOT COMMANDS
#=========

@bot.command(brief="test ping pong command")
async def ping(ctx):
    print("sending bitch")
    await ctx.send("bitch")

#===========
#SANIC COMMANDS
#==========
@app.route('/')
async def index(request):
    template = open(os.getcwd() + "/templates/index.html")
    return html(template.read())

@app.post('/spotauth')
async def spotauth(request):
    parameters = request.json
    cid = parameters['cid']
    secret = parameters['secret']
    username = parameters['username']
    
    print(f'the cid is {cid} the secret is {secret} the username is {username}')
    #handler = CacheFileHandler(cache_path=cache_path, username=username)
    handler = CacheFileHandler(cache_path=cache_path)
    #spotify_connections.append(spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri="http://10.100.1.90:8081", scope=scope, cache_handler=handler, open_browser=False)))
    #print(spotify_connections[0])
    #print(spotify_connections)
    #print(spotify_connections[0].user_playlists(username))
    return text(str(sp_oauth.get_authorize_url()))

@app.listener('after_server_start')
async def bot_startup(app, loop):
    loop.create_task(bot.start(TOKEN))

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    await bot.close()


#bot.run(TOKEN)
app.run(host='0.0.0.0', port=8081)

