import os
from google import genai


def generate_ai_plan(bmi, age, gender, category):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Create a simple 1-month diet and exercise plan.

BMI: {bmi}
Category: {category}
Age: {age}
Gender: {gender}

Keep it general, educational, and easy to follow.
Include:
1. Goal
2. Diet plan
3. Exercise plan
4. Weekly breakdown for 4 weeks
5. Safety note
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text if response.text else "No plan generated."