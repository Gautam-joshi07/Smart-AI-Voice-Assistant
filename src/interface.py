#

import os
import speech_recognition as sr
# import ffmpeg.audio
from elevenlabs import generate, play, set_api_key

# set_api_key(os.environ['ELEVEN_API_KEY'])
set_api_key(os.environ['ELEVEN_API_KEY' ] )

class AudioInterface:

    def listen(self) -> str:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something")
            # audio = recognizer.listen(source)
            audio = recognizer.listen(source,10,10)
        text = recognizer.recognize_whisper_api(
            audio,
            api_key=os.environ['OPENAI_API_KEY'],
        )

        return text


    def speak(self,text):
        audio = generate(
            text=text,
            voice='Bella',
            model='eleven_monolingual_v1'
        )
        play(audio)


#
#
#
#
#     def  speak(self,text):
#         audio = generate(
#             text=text,
#             voice='Bella',
#             model='eleven_monolingual_v1'
#         )
#         play(audio)

# import  os
# import speech_recognition as sr
#
# import  openai
# class AudioInterface:
#     def listen(self) -> str:
#         recognizer = sr.Recognizer
#         with sr.Microphone()  as source:
#             print("say some")
#             audio = recognizer.listen(source)
#
#         try:
#
#
#             text = recognizer.recognize_whisper_api(
#                 audio,
#                 api_key=os.environ['OPENAI_API_KEY'],
#             )
#             print("speech"+text)
#             return text
#
#         except sr.UnknownValueError:
#             print("not understand")
#
#         except sr.RequestError as e:
#             print(f"could not request")
#
#         return ""
#
# interface = AudioInterface()
# text = interface.listen()
# print(text)



    # def speak(self, text) -> str:
    #     pass

