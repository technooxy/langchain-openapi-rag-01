from gtts import gTTS
import os

# Text to be converted to speech
text = from google.cloud import texttospeech

# Initialize a Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Create an SSML request
ssml = """
    <speak>
        <prosody rate="slow">This is an example of SSML.</prosody>
        <p>You can control pitch, volume, and more.</p>
    </speak>
"""

# Convert SSML to audio
synthesis_input = texttospeech.SynthesisInput(ssml=ssml)
voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Wavenet-A")
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# Save the audio to a file
with open("output.mp3", "wb") as out_file:
    out_file.write(response.audio_content)


# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the speech as an MP3 file
tts.save("output.mp3")

# Play the saved MP3 file
os.system("start output.mp3")
