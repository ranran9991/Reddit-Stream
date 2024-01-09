import numpy as np
import requests
from src.transformers.consts import API_KEY, EMBEDDING_API_URL

headers = {"Authorization": f"Bearer {API_KEY}"}


class Embeddable:

    def __str__(self):
        return NotImplementedError()

    def embed(self) -> np.array:
        def query(payload):
            response = requests.post(EMBEDDING_API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": self.__str__(),
        })
        embedding = np.array(output)
        return embedding
