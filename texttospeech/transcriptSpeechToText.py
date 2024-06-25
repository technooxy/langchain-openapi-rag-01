import speech_recognition as sr

def transcribe_video_audio(video_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the video file
    with sr.AudioFile(video_path) as source:
        # Record the audio from the video
        audio = recognizer.record(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not request results; check your network connection"

# Specify the path to the video file
video_path = "your_video.mp4"

# Call the function to transcribe the audio from the video
transcribed_text = transcribe_video_audio(video_path)

# Print the transcribed text
print("Transcribed text from the video:")
print(transcribed_text)
