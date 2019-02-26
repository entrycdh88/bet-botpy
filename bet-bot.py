import asyncio
import discord
import openpyxl
client = discord.Client()
token = "NTQ0MzE1Nzc3NTQ5ODYwODc2.D1VaLg.NsznAICCL0pfbCAnrD5tVSxfz3g"
prefix = "off"
@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(game=discord.Game(name="Python으로 실행중입니다.", type=1))
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

    if message.content.startswith('ㅇ'):
        await client.send_message(channel, 'ㅇㅇ...')

    if message.content.startswith('ㅇㅇ'):
        await client.send_message(channel, 'ㅇㅇ...')

    if message.content.startswith('zzz'):
        await client.send_message(channel, 'zzz')
client.run(token)
