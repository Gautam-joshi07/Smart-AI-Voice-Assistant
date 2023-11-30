# from  dotenv import load_dotenv
# # from interface import AudioInterface
# from interface import AudioInterface
#
#
# load_dotenv()
#
# interface = AudioInterface()
# text = interface.listen()
# print(text)
#
# interface.speak(text)

from dotenv import load_dotenv
import  os
from agents import ConversationalAgent

load_dotenv()

# print(os.environ['OPENAI_API_KEY'])

from interface import AudioInterface
from agents import ConversationalAgent, SmartChatAgent

interface = AudioInterface()
agent = ConversationalAgent()
agent = SmartChatAgent()

while True:
    text = interface.listen()
    response = agent.run(text)
    # print(text)

    interface.speak(response)

