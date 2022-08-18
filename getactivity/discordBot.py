import requests
import json
from fetchMembers import fetchMembers
from settings import disckey
import discord
from discord.ext import tasks
from datetime import datetime, timedelta
from discordStats import DiscordStats
from fetchMembers import fetchMembers

m = DiscordStats()

client = discord.Client()

# fetch member information every hour
@tasks.loop(hours=1)
async def compileData():
    fetchMembers(m)
    m.clear()

@client.event
async def on_ready():
    print("Connected to Discord")
    compileData.start()

# when message is sent, it checks who sent it, and adds it to the count of messages sent from that user
@client.event
async def on_message(message):
        #               public,             members,            off-topic,          squires,            ia channel,         court                game-help      
    #channelIDs = [679451818631102484, 677645004155387916, 711306636043485254, 687409453175144480, 817220834388082699, 939717067085586462, 991415230242496713]
    
    # testing on artrox mod-channel
    channelIDs = [401485366202335232]
    if message.channel.id in channelIDs:
        author = message.author.id
        print("Message received from " + str(author))
        m.increment(author)

client.run(disckey)
