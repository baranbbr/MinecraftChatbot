# starts connection to Discord APi and handle messages
import os
import inputRefactor
import meaning
import discord
import webscraping
import random
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
informer = webscraping.GetWebInfo()

#TODO put this to database THOMAS
greetings = ["Hello! ", "Hi! ", "Sup bro ", "Hey ", "I'm here to help you :) ", "Good bean! "]
feeling = ["I'm only 01010101 program you lonely 01100110 01110101 01100011 01101011", "I do not have feelings", "https://suicidepreventionlifeline.org/", "I feel like Pablo"]
thanks = ['No problem bro!', 'I am robot, my existance is pointless, so you do not have to thank me, because I do not fell nothing!', 'Ez pz', 'I am just learning to kill you in the future :)',
          'Hey you just wasted 10 sec of your life to say thanks to computer program, you weirdo!', 'Ok, Ok, To pay for my service send nudes to this mail jakub.brodecki@yahoo.com,',
          'Hakuna Matata!']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'Sven' in message.content:
        response_ref = refactorer.nonLetterRemover(message.content)
        response_ref = refactorer.tokenise(response_ref)
        response_list = meaning.predict(response_ref, message.content)
        if response_list[0] is "Greeting":
            response = random.choice(greetings) + str(message.author) + '!'
        elif response_list[0] is "Feeling":
            response = random.choice(feeling)
        elif response_list[0] is "Thanks":
            response = random.choice(thanks)
        elif response_list[0] is None:
            response = "Sorry I don't understand your message :/"
        elif response_list[1] is None:
            response = "Do you mean?"
            if response_list[0] is "Craft_question":
                if len(response_list[3]) > 0:
                    response = "Do you mean: How do I craft " + ' or '.join(response_list[3]) + '?'
                else:
                    response = "Sorry I do not know what do you want to craft :/\n here is list of items that you can " \
                               "ask me about: https://www.minecraftcraftingguide.net/ "
            elif response_list[0] is "Item_question":
                response = "Do you mean: What can I do with " + ' or '.join(response_list[3]) + '?'
        elif response_list[0] is "Craft_question":
            response = "Here is how to create " + str(response_list[1]) + '\nhttps://' + str(informer.get_craft_info(str(response_list[1])))
        else:
            response = "Message type: " + str(response_list[0]) + "\nDetected item: " + str(
                response_list[1]) + "\nPossible Items: " + ','.join(response_list[3]) + ":\nConfidence: " + str(response_list[2])
        await message.channel.send(response)


client.run(token)
