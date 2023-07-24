#Scout Voice Assistant

Scout is a voice assistant designed to help you interact with your device hands-free. Scout is built using Python, leveraging several powerful libraries such as OpenAI for generating responses and ElevenLabs for voice synthesis.

##Installation

Before you can run Scout, you will need to install a few prerequisites.

Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/scout.git
```

Install the required Python libraries.

```bash
pip install -r requirements.txt
```

Set up your environment variables for the ElevenLabs and OpenAI API keys. In a Linux system, you can do this by adding the following lines to your .bashrc or .bash_profile:

```bash
export ELEVENLABS_API_KEY='your_eleven_labs_api_key_here'
export OPENAI_API_KEY='your_openai_api_key_here'
```

##Usage

To run Scout, simply create a new instance of the Scout class and call the start method.

```python
from scout import Scout

scout = Scout(audio_device_index=0, voice_name="roboBrit")
scout.start()
```

Replace audio_device_index=0 with the index of your actual audio device. The voice_name parameter can be used to specify the voice to use for the assistant's responses.