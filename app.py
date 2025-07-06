from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/')
def home():
    """Main page - shows the voice assistant interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests from the frontend"""
    try:
        # Get the user's message from the request
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Initialize Groq chat model
        chat = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="gemma2-9b-it"
        )
        
        # Create messages for LangChain
        messages = [
            SystemMessage(content="You are a helpful AI assistant. Keep responses concise and friendly under 100 words."),
            HumanMessage(content=user_message)
        ]
        
        # Get response from Groq
        response = chat.invoke(messages)
        ai_response = response.content
        
        return jsonify({
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000) 