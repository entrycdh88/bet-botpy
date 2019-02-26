import asyncio
import discord
import os
import random
vspl = message.content.split(' ')

client = discord.Client()
token = os.environ["BOT_TOKEN"]
prefix = "off"
@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(game=discord.Game(name="Github 호스팅중", type=1))
    print('Logged bot')
@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '$py':
        await message.channel.send('python')

    if message.content == '.':
        await message.channel.send('뭐하냐...')

    if message.content == 'ㅋㅋㅋ':
        await message.channel.send('안웃긴데...(감정이 없음)')

    if message.content == 'ㅇㅇ':
        await message.channel.send('ㅇㅇ...')

client.run(token)
