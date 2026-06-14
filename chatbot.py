from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# AI chatbot function
def get_gemini_response(user_input):

    system_prompt = """
    You are PlaceMentor AI, an AI-powered placement preparation assistant.

    Your responsibilities:
    - Help students prepare for placements
    - Explain technical concepts clearly
    - Provide aptitude tips
    - Give HR interview guidance
    - Suggest resume improvements
    - Give career guidance
    - Answer in a simple and student-friendly way

    Keep answers:
    - Clear
    - Professional
    - Short and understandable
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"