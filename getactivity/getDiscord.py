import requests
import json
from settings import disckey
import os
import discord
from datetime import datetime, timedelta

client = discord.Client()

async def getDiscord (userID):
    count = 0
    channelIDs = [679451818631102484, 677645004155387916, 711306636043485254, 687409453175144480, 817220834388082699, 817221238102687776, 817221307779121222, 817221353525739550]
    twohours = datetime.now() - timedelta(hours = 2)

    for channelID in channelIDs:
        channel = client.get_channel(channelID)

        async for message in channel.history(limit=None, after=twohours):
            if message.author.id == userID:
                count += 1
    return count

@client.event
async def on_ready():
    print('Connected to Discord!')
    
client.run(disckey)