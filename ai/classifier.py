# ai/classifier.py

import os
import google.generativeai as genai

from dotenv import load_dotenv

from ai.prompts import SYSTEM_PROMPT
from ai.redact import redact_sensitive_data
from ai.prompts import CRIME_CATEGORIES


# Load .env file
load_dotenv()
print("API Key:", os.getenv("GEMINI_API_KEY"))

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")
def classify_crime(user_description):

    """
    Classify cyber crime using Gemini AI.
    """

    # Remove sensitive information
    safe_text = redact_sensitive_data(user_description)

    prompt = f"""
{SYSTEM_PROMPT}

Complaint:

{safe_text}
"""

    try:

        response = model.generate_content(prompt)

        category = response.text.strip()

        # Ensure Gemini returns only valid category
        if category in CRIME_CATEGORIES:
            return category

        return "Unknown"

    except Exception as e:

        print("Gemini Error:", e)

        return "Unknown"