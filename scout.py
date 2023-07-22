import pvporcupine
from threading import Thread
from pvleopard import create, LeopardActivationLimitError
from pvrecorder import PvRecorder
import openai
from elevenlabs import generate, play, set_api_key
import os

class Scout(Thread):
    def __init__(self, audio_device_index):
        super().__init__()
        self._audio_device_index = audio_device_index
        eleven_labs_api_key= os.environ["ELEVEN_LABS_API_KEY"]
        set_api_key(eleven_labs_api_key)
        openai.api_key = os.environ["OPENAI_API_KEY"]
        porcupine_access_key = os.environ["PORCUPINE_ACCESS_KEY"]
        voice_name= "roboBrit"

    def start(self):
        scout = pvporcupine.create(
            access_key=self.porcupine_access_key,
            keywords=['scout']
        )
        while True:
            recorder = PvRecorder(frame_length=scout.frame_length, device_index=self._audio_device_index)
            recorder.start()
            pcm = recorder.read()
            result = scout.process(pcm)
            if result >= 0:
                human = self.get_human_response()
                ai = self.get_ai_response(human)
                self.get_voice(ai)


    def get_human_response(self, recorder):
        leopard = create(access_key='${ACCESS_KEY}')
        try:
            human_request, words = leopard.process(recorder.stop())
            transcript = human_request
        except LeopardActivationLimitError:
                human_request = 'AccessKey has reached its processing limit.'
    
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
    