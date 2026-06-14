import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# AI Response Function
def get_gemini_response(user_input):

    try:

        # Generate AI Response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are PlaceMentor AI,
                    an AI-powered placement preparation assistant.

                    Help students with:
                    - Technical Interview Preparation
                    - Aptitude Questions
                    - HR Interview Questions
                    - Resume Tips
                    - Career Guidance

                    Give clear and professional answers.
                    """
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],

            # Updated Groq Model
            model="llama-3.3-70b-versatile",

            temperature=0.7,
            max_tokens=1024
        )

        # Return AI Response
        return chat_completion.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"

