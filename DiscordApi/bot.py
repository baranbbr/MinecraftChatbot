import os
import discord
from dotenv import load_dotenv
import messageHandler

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
messageHandler = messageHandler.MessageHandler()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'Sven' in message.content:
        response = messageHandler.generate_response(message.content, message.author)
        await message.channel.send(response)

client.run(token)
