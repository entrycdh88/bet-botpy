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

    id = message.author.id
    channel = message.channel

    if message.content == '$py':
        await message.channel.send('python')

    if message.content == '.':
        await message.channel.send('뭐하냐...')

    if message.content == 'ㅋㅋㅋ':
        await message.channel.send('안웃긴데...(감정이 없음)')

    if message.content == 'ㅇㅇ':
        await message.channel.send('ㅇㅇ...')

    if message.content == 'zzz':
        await message.channel.send('zzz')

    if message.content == '수류탄':
        await message.channel.send('킹감자')

    if message.content == '랩터':
        await message.channel.send('PRO YOUTUBER RAPTORLEE')

    if message.content == '매니저':
        await message.channel.send('無')

    if message.content == '배그':
        await message.channel.send('Player Unknown Batle Ground')

    if message.content == '슬찬':
        await message.channel.send('PRO YOUTUBER RAPTORLEE')

    if message.content == '팬타':
        await message.channel.send('???: 키킥 넷마블~')

    if message.content == '랩터':
        await message.channel.send('PRO YOUTUBER RAPTORLEE')

    if message.content == '라면':
        await message.channel.send('꼬불꼬불 맛좋은 라면~~')

    if message.content == '에임갓':
        await message.channel.send('반대로 에임ㄸ...')

    
client.run(token)
