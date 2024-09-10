import openai

openai.api_key = 'your_openai_api_key'

def generate_story(theme, age_group, length="short"):
    """ Generate a story based on theme and age group """
    prompt = f"Tell a {length} story for a {age_group}-year-old child about {theme}. The story should be fun and engaging."
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8
    )
    story = response.choices[0].text.strip()
    return story

# Example Usage
theme = "a brave little fox"
age_group = 6
story = generate_story(theme, age_group)
print("Generated Story: ", story)
