from fastapi import FastAPI, Request
from pydantic import BaseModel
from story_generation import generate_story
from story_translation import translate_story

app = FastAPI()

class StoryRequest(BaseModel):
    theme: str
    age_group: int

@app.post("/api/generate-story")
async def create_story(request: StoryRequest):
    story = generate_story(request.theme, request.age_group)
    return {"story": story}

@app.post("/api/translate-story")
async def translate_story_endpoint(request: StoryRequest):
    translated_story = translate_story(request.theme, 'fi')
    return {"translated_story": translated_story}
