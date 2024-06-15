import os

class ConfigClass():
    """Class to import secrets values"""

    @property
    def openai_api_key(self) -> None:
        """Import OpenAI API key"""
        os.getenv("OPENAI_API_KEY")

    @property
    def gemini_api_key(self) -> None:
        """Import Google Gemini API Key"""
        os.getenv("GEMINI_API_KEY")

    @property
    def llama_api_key(self) -> None:
        """Import Meta Llama API Key"""
        os.getenv("LLAMA_API_KEY")


config = ConfigClass()
