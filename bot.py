import discord
from discord.ext import commands 
import asyncio
#import youtube_dl
import shutil
import os 
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

players = {}

@client.event
async def on_ready():
    print('System is Online, Welcome to Pootie Music Bot')

 #/help manual
@client.command(aliases=['hi'])
async def hello(ctx):
    user = ctx.message.author
    await ctx.send(f"Hello There {user.mention}, here is the help manual:")


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    Voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
server = ctx.message.server
voice_client = client.voice_client_in(server)
player = await voice_client.music_player(url)
players[server.id] = player
player.start()

@client.command(pass_context=True)
async def pause(ctx)
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx)
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx)
    id = ctx.message.server.id
    players[id].resume()

client.run('NzE5OTc4MDMxNjk0NzQxNTYy.XuBwKw.QTnCdrRXJpI6kcFOvDRTvklTy-g')
