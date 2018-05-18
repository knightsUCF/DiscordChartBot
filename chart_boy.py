#!/usr/bin/python3


# 1. Create an app: https://discordapp.com/developers/applications/me
# 2. Create "Bot User"
# 3. Get token (not secret key) after creating Bot User
# 4. Select "Public Bot"
# 5. Replace the CLIENTID in the following link with your bot's client ID and go to url: https://discordapp.com/oauth2/authorize?client_id=CLIENTID&scope=bot



# libs

import asyncio
import discord
import tempfile
from discord.ext.commands import Bot
from discord.ext import commands


# scraping

import urllib.request


# image processing

from io import BytesIO
from PIL import Image, ImageDraw



# authorization

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


token = 'token_ID'



# retrieve chart

def get_image_from_url(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, 'sc.jpg')
    img = Image.open('sc.jpg').convert('RGB')
    img.save('sc', 'JPEG')



# deploy to discord w/ asynchronous callers


@client.event 
async def on_ready():
    print("Connection established") 



@client.event
async def on_message(message):

    if message.content == "!chart eurusd": # or "!chart EURUSD" or "!chart EUR/USD":
        url = 'http://stockcharts.com/c-sc/sc?s=%24EURUSD&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart gbpusd":
        url = 'http://stockcharts.com/c-sc/sc?s=%24GBPUSD&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart usdjpy":
        url = 'http://stockcharts.com/c-sc/sc?s=%24USDJPY&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart audusd":
        url = 'http://stockcharts.com/c-sc/sc?s=%24AUDUSD&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart usdchf":
        url = 'http://stockcharts.com/c-sc/sc?s=%24USDCHF&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart eurgbp":
        url = 'http://stockcharts.com/c-sc/sc?s=%24EURGBP&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart usdcad":
        url = 'http://stockcharts.com/c-sc/sc?s=%24USDCAD&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')

    if message.content == "!chart eurjpy":
        url = 'http://stockcharts.com/c-sc/sc?s=%24EURJPY&p=D&yr=0&mn=1&dy=0&i=t45717241791&r=1526237067538'
        get_image_from_url(url)
        await client.send_file(message.channel, 'sc.jpg')



client.run(token)



