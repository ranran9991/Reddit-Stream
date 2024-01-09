import enum
import requests
from typing import List
from collections import Counter
from src.transformers.consts import API_KEY, SENTIMENT_API_URL

headers = {"Authorization": f"Bearer {API_KEY}"}


class Sentiment(enum.Enum):
    positive = 1
    neutral = 0
    negative = -1


def extract_sentiment(text: str) -> Sentiment:
    def query(payload):
        response = requests.post(SENTIMENT_API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": text,
    })
    sentiment = output[0][0]['label']
    return Sentiment[sentiment]


def aggregate_sentiment(sentiments: List[Sentiment]) -> Sentiment:
    counter = Counter(sentiments)
    most_common = counter.most_common()[0][0]
    return most_common
