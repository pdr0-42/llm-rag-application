import os

class ConfigClass:
    """Class to import secrets values"""

    @property
    def openai_api_key(self) -> None:
        """Import OpenAI API key"""
        api_key = os.getenv("OPENAI_API_KEY")
        return api_key

    @property
    def openai_model(self) -> None:
        """Import OpenAI model"""
        llm = os.getenv("OPENAI_MODEL")
        return llm

    @property
    def openai_vector_store(self) -> None:
        """Import """
        vector_store = os.getenv("OPENAI_VECTOR_STORE_ID")
        return vector_store



config = ConfigClass()
