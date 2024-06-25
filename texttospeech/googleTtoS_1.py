from google.cloud import texttospeech

# Initialize a Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Create an SSML request
ssml = """
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-IN">
        <voice name="en-IN-NeerjaNeural">
            This is an example of SSML with an Indian male voice.
            Adjust the emphasis, speaking rate, pitch, and volume as needed.
        </voice>
    </speak>
"""

# Convert SSML to audio
synthesis_input = texttospeech.SynthesisInput(ssml=ssml)
#voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Wavenet-A")
voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-IN-NeerjaNeural")
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# Save the audio to a file
with open("output.mp3", "wb") as out_file:
    out_file.write(response.audio_content)
