import requests
import json
from settings import disckey
import os
import discord
from dotenv import load_dotenv
from datetime import datetime, timedelta

client = discord.Client()

async def getDiscord (userID):
    channelID = 401485366202335232

    channel = client.get_channel(channelID)
    twohours = datetime.now() - timedelta(hours = 2)

    count = 0
    async for message in channel.history(limit=None, after=twohours):
        if message.author.id == userID:
            count += 1
    return count

@client.event
async def on_ready():
    print('Connected to Discord!')
    count = await getDiscord(149622767317155840)
    print(count)


client.run(disckey)