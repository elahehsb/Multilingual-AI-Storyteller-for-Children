from googletrans import Translator

def translate_story(story_text, target_language='fi'):
    """ Translate the story into a target language """
    translator = Translator()
    translation = translator.translate(story_text, dest=target_language)
    return translation.text

# Example Usage
translated_story = translate_story(story, 'fi')  # Translate to Finnish
print("Translated Story: ", translated_story)
