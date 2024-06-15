from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI


class LLMConnector(ABC):
    """
    Abstract base class for LLM connectors. Requires the implementation
    of the connect method in subclasses.
    """
    def __init__(self, api_key: str, model: str, temperature: float = 0.0) -> None:
        self._api_key = api_key
        self._model = model
        self._temperature = temperature

    @property
    def api_key(self) -> str:
        """Returns the API key."""
        return self._api_key

    @property
    def model(self) -> str:
        """Returns the model name."""
        return self._model

    @property
    def temperature(self) -> float:
        """Returns the temperature setting."""
        return self._temperature

    @abstractmethod
    def connect(self):
        """Connect to the respective LLM. Must be implemented by subclasses."""
        pass


class OpenAIConnector(LLMConnector):
    """
    Connector for OpenAI's LLM.
    """
    def connect(self) -> ChatOpenAI:
        """Connect to OpenAI LLM."""
        return ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=self.api_key
        )


class GeminiConnector(LLMConnector):
    """
    Connector for Google's Gemini LLM.
    """
    def connect(self) -> ChatGoogleGenerativeAI:
        """Connect to Google Gemini LLM."""
        return ChatGoogleGenerativeAI(
            model=self.model,
            google_api_key=self.api_key,
            temperature=self.temperature
        )


class LlamaConnector(LLMConnector):
    """
    Connector for Meta's Llama LLM.
    """
    def connect(self) -> ChatLlamaAPI:
        """Connect to Meta Llama LLM."""
        llama = LlamaAPI(self.api_key)
        return ChatLlamaAPI(client=llama)


class LLMFactory:
    """
    Factory class for creating LLM connectors based on the specified type.
    """
    @staticmethod
    def create_connector(llm_type: str, api_key: str, model: str = "default", temperature: float = 0.0) -> LLMConnector:
        """
        Create and return an LLM connector based on the specified type.
        
        Args:
            llm_type (str): The type of LLM (e.g., 'openai', 'gemini', 'llama').
            api_key (str): The API key for the LLM service.
            model (str): The model name to use for the LLM.
            temperature (float): The temperature setting for the LLM.

        Returns:
            LLMConnector: An instance of a subclass of LLMConnector.

        Raises:
            ValueError: If the specified llm_type is not recognized.
        """
        connectors = {
            "openai": OpenAIConnector,
            "gemini": GeminiConnector,
            "llama": LlamaConnector
        }
        connector_class = connectors.get(llm_type)
        if not connector_class:
            raise ValueError(f"Unknown LLM type: {llm_type}")
        return connector_class(api_key, model, temperature)
    
