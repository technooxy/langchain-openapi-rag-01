import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Convert text to speech
text="""Is this the first time we are meeting , welcome to my channel Enpakkam.
My name is RJ , this site helps career wise to grow further.
dont miss my future updates , for that press the like button and subscribe to my channel."""



ssml_text = """
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-IN">
        <voice name="fr-FR-DeniseNeural">
            This is an example of SSML with an Indian male voice.
            Adjust the emphasis, speaking rate, pitch, and volume as needed.
        </voice>
    </speak>
"""

engine.say(ssml_text)
engine.runAndWait()
