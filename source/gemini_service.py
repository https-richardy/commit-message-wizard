# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from .configuration import Configuration
import google.generativeai as gemini

class GeminiService:
    def __init__(this, configuration: Configuration):
        this.configuration = configuration
        this.generative_model_name = "gemini-1.5-flash"

        gemini.configure(this.configuration.api_key)
        this.model = gemini.GenerativeModel(this.generative_model_name)

    def get_response(this, prompt: str) -> str:
        response = this.model.generate_content(prompt)
        return response.text