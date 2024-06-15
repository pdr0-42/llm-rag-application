from langchain_openai import ChatOpenAI


class OpenAIConnector:
    """Class to run a connection to OpenAI Large Language Model"""

    def __init__(self, api_key:str, llm_model:str) -> None:
        self._api_key = api_key
        self._llm_model = llm_model

    @property
    def api_key(self) -> str:
        """Return OpenAI token"""
        return self._api_key

    @property
    def llm_model(self) -> str:
        """Return which Large Language Model is will be used"""
        return self._llm_model

    def connect(self) -> ChatOpenAI:
        """Connect to OpenAI Large Language Model.
        
        Returns:
            ChatOpenAI: An instance of connection to OpenAI
        """
        return ChatOpenAI(
            model=self.llm_model,
            temperature=0.0,
            api_key=self.api_key
        )
