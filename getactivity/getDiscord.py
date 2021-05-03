import requests
import json
from settings import disckey
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv(disckey)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)