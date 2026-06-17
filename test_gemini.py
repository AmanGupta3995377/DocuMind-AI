from llm.gemini_adapter import GeminiAdapter

gemini = GeminiAdapter()

response = gemini.generate_response(
    "Explain cybersecurity management in 3 lines."
)

print(response)