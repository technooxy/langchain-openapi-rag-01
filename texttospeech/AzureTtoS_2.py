import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription='993cf66d5e99434b8fac3d7c75fb5272', 
                                       region='eastus')
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#working 
#es-ES-ElviraNeural (Malay female voice)
# en-US-AvaMultilingualNeural1 (Female)

#Not working
#AIGenerate2
# en-US-AndrewMultilingualNeural1 (Male)

# en-US-BrianMultilingualNeural1 (Male)
# en-US-EmmaMultilingualNeural1 (Female)
# The neural multilingual voice can speak different languages based on the input text.
# en-PH-JamesNeural (Male) - filiphino good one
# en-IN-PrabhatNeural good indian
# ta-IN-PallaviNeural (Female) tamil
# ta-IN-ValluvarNeural (Male) tamil

speech_config.speech_synthesis_voice_name='en-PH-JamesNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.

text = """This is an example of SSML with an Indian male voice.
            Adjust the emphasis, speaking rate, pitch, and volume as needed."""

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")