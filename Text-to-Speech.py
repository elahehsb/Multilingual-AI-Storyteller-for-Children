from gtts import gTTS
import os

def text_to_speech(story_text, language='en'):
    """ Convert text to speech using Google Text-to-Speech """
    tts = gTTS(text=story_text, lang=language)
    tts.save("story.mp3")
    os.system("start story.mp3")

# Example Usage
text_to_speech(translated_story, 'fi')  # Play story in Finnish
