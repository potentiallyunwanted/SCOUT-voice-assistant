import pvporcupine
import pvleopard
import openai
from elevenlabs import generate, play, set_api_key
import os

class Scout:
    def __init__(self):
        eleven_labs_api_key= os.environ["ELEVEN_LABS_API_KEY"]
        set_api_key(eleven_labs_api_key)
        openai.api_key = os.environ["OPENAI_API_KEY"]
        porcupine_access_key = os.environ["PORCUPINE_ACCESS_KEY"]
        voice_name= "roboBrit"
    
    def get_next_audio_frame():
        pass

    def wake_up(self):
        scout = pvporcupine.create(
            access_key=self.porcupine_access_key,
            keywords=['scout']
        )
        while True:
            audio_frame = self.get_next_audio_frame()
            keyword_index = scout.process(audio_frame)
            if keyword_index == 0:
                human = self.get_human_response()
                ai = self.get_ai_response(human)
                self.get_voice(ai)


    def get_human_response(self, audio_path):
        
        leopard = pvleopard.create(access_key='${ACCESS_KEY}')

        transcript, words = leopard.process_file(audio_path)
        for word in words:
            print(
            "{word=\"%s\" start_sec=%.2f end_sec=%.2f confidence=%.2f}"
            % (word.word, word.start_sec, word.end_sec, word.confidence))
        return transcript

    def get_ai_response(self, input):
        # create a chat completion
        chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": input}])
        # print the chat completion
        response_text = chat_completion.choices[0].message.content
        return response_text

    def get_voice(self, text):
        audio = generate(text=text, voice=self.voice_name)
        play(audio)
    