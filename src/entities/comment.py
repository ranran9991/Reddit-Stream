from dataclasses import dataclass
from src.transformers.embedding import Embeddable
from processor import process_json_data


@dataclass
class Comment(Embeddable):
    author: str
    created_utc: str
    body: str
    post_id: str
    comment_id: str

    def __str__(self):
        return self.body

    def to_protocolized_message(self):
        content_value = self.__str__()
        source = 'posts'
        time = self.created_utc
        message = process_json_data(content_value, source, time)
        return message
