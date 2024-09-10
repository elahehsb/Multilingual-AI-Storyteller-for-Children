import React, { useState } from 'react';
import axios from 'axios';

const StoryTeller = () => {
    const [theme, setTheme] = useState("");
    const [ageGroup, setAgeGroup] = useState(6);
    const [story, setStory] = useState("");
    
    const handleGenerateStory = async () => {
        const response = await axios.post('/api/generate-story', { theme, ageGroup });
        setStory(response.data.story);
    };

    return (
        <div>
            <h1>Multilingual AI Storyteller</h1>
            <input 
                type="text" 
                value={theme} 
                onChange={(e) => setTheme(e.target.value)} 
                placeholder="Enter a theme"
            />
            <button onClick={handleGenerateStory}>Generate Story</button>

            {story && (
                <div>
                    <h2>Your Story</h2>
                    <p>{story}</p>
                </div>
            )}
        </div>
    );
};

export default StoryTeller;
