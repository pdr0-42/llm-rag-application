import openai
from utilities.config import config
from llm_connector import OpenAIConnector

class RetrieverAugmentedGenerate:
    def __init__(self) -> None:
        self.llm = OpenAIConnector(
            api_key=config.openai_api_key,
            llm_model=config.openai_model
            )
        self._vector_store_id = config.openai_vector_store
        self._model = config.openai_vector_store

    def get_embeddings(self, text: str):
        """"""
        response = openai.embeddings.create(
            model=self.llm.llm_model,
            input=text
        )
        return response['data'][0]['embeddings']