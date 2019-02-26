import asyncio
import discord
import os
word = []
comq = []
coma = []
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
        await client.send_message(channel, 'python')

    if message.content.startswith('.'):
        await client.send_message(channel, '뭐하냐...')

    if message.content.startswith('ㅋㅋㅋ'):
        await client.send_message(channel, '안웃긴데...(감정이 없음)')

    if message.content.startswith('ㅇㅇ'):
        await client.send_message(channel, 'ㅇㅇ...')

    if message.content.startswith('zzz'):
        await client.send_message(channel, 'zzz')
       
    if message.content.startswith('ah'):
        await client.send_message(channel, 'ㅏㅏㅏㅏㅏ')
        
    if message.content.word[0] == '$':
        n = 0
        for i in comq:
            if message.content == i:
                await client.send_message(channel, coma[n])
                break
            n = n + 1
            
     if message.content.startsWith('명령어 추가'):
        comq.append('$' + vspl[2])
        coma.append(vspl[3])
        await client.send_message(channel, '명령어가 추가 됐습니다.')
        
client.run(token)
