from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI


class LLMConnector(ABC):
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def api_key(self) -> str:
        return self._api_key

    @abstractmethod
    def connect(self):
        pass


class OpenAIConnector(LLMConnector):
    def connect(self) -> ChatOpenAI:
        """Connect to OpenAI LLM"""
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            api_key=self.api_key
        )
        return llm


class GeminiConnector(LLMConnector):
    def connect(self) -> ChatGoogleGenerativeAI:
        """Connect to Google Gemini LLM"""
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=self.api_key,
            temperature=0.0
        )
        return llm


class LlamaConnector(LLMConnector):
    def connect(self) -> ChatLlamaAPI:
        """Connect to Meta Llama LLM"""
        llama = LlamaAPI(self.api_key)
        model = ChatLlamaAPI(client=llama)
        return model


class LLMFactory:
    @staticmethod
    def create_connector(llm_type: str, api_key: str) -> LLMConnector:
        if llm_type == "openai":
            return OpenAIConnector(api_key)
        elif llm_type == "gemini":
            return GeminiConnector(api_key)
        elif llm_type == "llama":
            return LlamaConnector(api_key)
        else:
            raise ValueError(f"Unknown LLM type: {llm_type}")

