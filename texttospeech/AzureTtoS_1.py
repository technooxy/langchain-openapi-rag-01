import os
import azure.cognitiveservices.speech as speechsdk

# Set up the Speech SDK configuration
speech_config = speechsdk.SpeechConfig(
    subscription='993cf66d5e99434b8fac3d7c75fb5272',  # Replace with your actual Speech resource key
    region='eastus'  # Replace with your actual Speech resource region
)

# MALE_VOICE_NAME_HINDI = "hi-IN-KalpanaNeural"
# #speech_config.speech_synthesis_language = "en-US"
#AIGenerate1
#AIGenerate2
# en-US-AndrewMultilingualNeural1 (Male)
# en-US-AvaMultilingualNeural1 (Female)
# en-US-BrianMultilingualNeural1 (Male)
# en-US-EmmaMultilingualNeural1 (Female)

speech_config.speech_synthesis_voice_name = "en-US-EmmaMultilingualNeural1"




# Set the text to be synthesized
text_to_speak = "Hello, this is an example of text-to-speech using Azure Speech Service."

#hindi_text = "यह एक टेस्ट वाक्य है।"
#audio_config = speechsdk.AudioOutputConfig(filename="output.mp3")
# Create a speech synthesis client
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
#synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


# Synthesize the text
result = synthesizer.speak_text_async(text_to_speak).get()


# Check if synthesis was successful
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesis successful. Audio saved to output.wav")
else:
    print(f"Speech synthesis failed: {result.reason}")

# Save the synthesized audio to a file
output_file = "synthesized_audio.wav"
#result.audio.to_wav_file(output_file)
with open(output_file, "wb") as audio_file:
    audio_file.write(result.audio_data)
print(f"Audio saved to {output_file}")
