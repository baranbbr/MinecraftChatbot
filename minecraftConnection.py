from mcpi.minecraft import Minecraft
import time
import inputRefactor
import meaning
import webscraping

refactorer = inputRefactor.inputRefactor()
meaning = meaning.Meaning()
informer = webscraping.GetWebInfo()
#need to provide server id and port here
mc = Minecraft.create("51.83.46.159", 4711)
print("hello")

class Connection:

    @classmethod
    def edited_on_message(self, message):
        playerID = message.entityId
        message = message.message
        if 'Sven' in message:
            response_ref = refactorer.nonLetterRemover(message)
            response_ref = refactorer.tokenise(response_ref)
            response_list = meaning.predict(response_ref, message)
            if response_list[0] is "Greeting":
                response = "Hello " + str(playerID) + '!'
            elif response_list[0] is None:
                response = "Sorry I don't understand your question :/"
            elif response_list[1] is None:
                response = "Do you mean?"
                if response_list[0] is "Craft_question":
                    response = "Do you mean: How do I craft " + ' or '.join(response_list[3]) + '?'
                elif response_list[0] is "Item_question":
                    response = "Do you mean: What can I do with " + ' or '.join(response_list[3]) + '?'
            elif response_list[0] is "Craft_question":
                response = "Here is how to create " + str(response_list[1]) + 'https://' + str(
                    informer.get_craft_info(str(response_list[1])))
            else:
                response = "Message type: " + str(response_list[0]) + "Detected item: " + str(response_list[1]) + "Possible Items: " + ','.join(response_list[3]) + ":Confidence: " + str(response_list[2])
            mc.postToChat(response)

while True:
    for posts in mc.events.pollChatPosts():
        Connection.edited_on_message(posts)
    time.sleep(1)


