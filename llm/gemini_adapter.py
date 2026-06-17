import os

from dotenv import load_dotenv
import google.generativeai as genai


class GeminiAdapter:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "models/gemini-2.5-flash"
        )

        print(
            "Gemini Adapter Initialized"
        )

    def generate_response(
        self,
        prompt
    ):

        response = self.model.generate_content(
            prompt
        )

        return response.text