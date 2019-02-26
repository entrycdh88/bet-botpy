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

    if message.content.startswith('$py'):
        await message.channel.send('python')

    if message.content.startswith('.'):
        await client.send_message(channel, '뭐하냐...')

    if message.content.startswith('ㅋㅋㅋ'):
        await client.send_message(channel, '안웃긴데...(감정이 없음)')

    if message.content.startswith('ㅇㅇ'):
        await client.send_message(channel, 'ㅇㅇ...')

    if message.content.startswith('zzz'):
        await client.send_message(channel, 'zzz')

    if message.content.startsWith('수류탄'):
        await client.send_message(channel, '킹감자')

    if message.content.startsWith('랩터'):
        await client.send_message(channel, 'PRO YOUTUBER RAPTORLEE')

    if message.content.startsWith('매니저'):
        await client.send_message(channel, '無')

    if message.content.startsWith('배그'):
        await client.send_message(channel, 'Player Unknown Batle Ground')

    if message.content.startsWith('슬찬'):
        await client.send_message(channel, 'PRO YOUTUBER RAPTORLEE')

    if message.content.startsWith('팬타'):
        await client.send_message(channel, '???: 키킥 넷마블~')

    if message.content.startsWith('랩터'):
        await client.send_message(channel, 'PRO YOUTUBER RAPTORLEE')

    if message.content.startsWith('라면'):
        await client.send_message(channel, '꼬불꼬불 맛좋은 라면~~')

    if message.content.startsWith('에임갓'):
        await client.send_message(channel, '반대로 에임ㄸ...')

    
client.run(token)
