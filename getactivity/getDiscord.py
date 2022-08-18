import requests
import json
from settings import disckey
import os
import discord
from datetime import datetime, timedelta

client = discord.Client()

# input Discord userID, return amount of messages sent
async def getDiscord (userID):
    print(1)
    client.run(disckey)
    print(2)
    # run bot using discord api key
    count = 0
    #               public,             members,            off-topic,          squires,            ia channel,         court                game-help      
    #channelIDs = [679451818631102484, 677645004155387916, 711306636043485254, 687409453175144480, 817220834388082699, 939717067085586462, 991415230242496713]

    # testing on artrox mod-channel
    channelIDs = [401485366202335232]
    twohours = datetime.now() - timedelta(hours = 2)

    print("Counting messages for " + str(userID))
    # Go through all channels in channelIDs
    for channelID in channelIDs:
        channel = client.get_channel(channelID)
        
        # Retrieve all messages in iterated channel in the last two hours by userID
        async for message in channel.history(limit=None, after=twohours):
            if message.author.id == userID:
                count += 1

    print(count)
    await client.close()
    return count


    # test
    # await getDiscord(149622767317155840)
    

