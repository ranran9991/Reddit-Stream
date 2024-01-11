from dataclasses import dataclass
from src.transformers.embedding import Embeddable
from processor import process_json_data


@dataclass
class Post(Embeddable):
    post_id: str
    title: str
    content: str
    author: str
    created_utc: float  # in timestamp format
    url: str

    def __str__(self):
        out = f'{self.title}\n{self.content}'
        return out

    def to_protocolized_message(self):
        content_value = self.__str__()
        source = 'posts'
        time = self.created_utc
        message = process_json_data(self.post_id, content_value, source, time)
        return message
