# Voice AI Assistant

A simple voice-based AI assistant that listens to your voice, processes it with AI, and speaks back the response.

## Quick Start

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Groq API Key
1. Go to [Groq Console](https://console.groq.com/keys)
2. Create an account and get your API key
3. Copy the API key

### 3. Set Up Environment
1. Open `.env`
2. Replace `your_groq_api_key_here` with your actual API key

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
Go to: `http://localhost:9000`

## How to Use

1. **Click the microphone button** to start recording
2. **Speak your question** clearly
3. **Wait for the AI response**  it will speak back to you!
4. **Click the microphone again** to ask another question
5. **Pause** to interrupt agent in between
6. **Stop conversation** to end the conversation

## Files Explained

- `app.py` - Flask backend server
- `templates/index.html` - Frontend webpage with voice controls
- `requirements.txt` - Python packages needed
- `env_template.txt` - Template for your API key

## Features

- Voice input using browser microphone
- Speech-to-text conversion
- AI processing with Groq (LangChain)
- Text-to-speech response
- Conversation transcript display
- Simple, beginner-friendly interface

## Troubleshooting

**"Speech recognition not supported"**
- Use Chrome, Edge, or Safari browser
- Make sure you allow microphone access

**"Error processing request"**
- Check your Groq API key is correct
- Make sure you have internet connection

**Microphone not working**
- Click the lock icon in your browser address bar
- Allow microphone access for this site

## Tips

- Speak clearly and at a normal pace
- Keep questions simple for best results
- The AI will speak back the response automatically
- You can see the full conversation in the transcript area 
