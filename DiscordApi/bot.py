# starts connection to Discord APi and handle messages
import os
import inputRefactor
import meaning
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

refactorer = inputRefactor.InputRefactor()
meaning = meaning.Meaning()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'Sven' in message.content:
        response_ref = refactorer.nonLetterRemover(message.content)
        response_ref = refactorer.tokenise(response_ref)
        response_list = meaning.predict(response_ref, message.content)
        if response_list[0] == "Greeting":
            response = "Hello " + str(message.author) + '!'
        elif response_list[0] == None:
            response = "Sorry I don't understand your question :/"
        else:
            response = "Message type: " + str(response_list[0]) + "\nDetected item: " + str(response_list[1]) + "\nConfidence: " + str(response_list[2])
        await message.channel.send(response)


client.run(token)
