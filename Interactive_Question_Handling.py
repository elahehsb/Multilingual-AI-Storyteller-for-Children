import openai
import speech_recognition as sr

def listen_for_question():
    """ Use speech recognition to capture user's question """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask a question...")
        audio = recognizer.listen(source)
        question = recognizer.recognize_google(audio)
    return question

def answer_question(question, story):
    """ Generate an answer using GPT-4 based on the question and story context """
    prompt = f"The story is: {story}. Now, a child asks the question: {question}. How would you answer in a simple way?"
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Example Usage
question = listen_for_question()
answer = answer_question(question, story)
print("AI Response: ", answer)
