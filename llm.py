import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def render_answer(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a tutor. Follow the given strategy exactly."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content
