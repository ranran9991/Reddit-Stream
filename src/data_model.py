import json
from uuid import UUID
from typing import List, Any
from dataclasses import dataclass


@dataclass
class PipelineContext:
    item_id: UUID


class ContextElement:
    type: str
    value: str

    def __init__(self, context_type: str, value: str) -> None:
        self.type = context_type
        self.value = value

    def to_dict(self):
        return {'type': self.type, 'value': self.value}


@dataclass
class General:
    end_time: int
    item_id: UUID
    start_time: int
    sub_type: str
    system_time: int
    type: str
    source_application: str


class Content:
    value: None
    ref: str

    def __init__(self, value: None, ref: str) -> None:
        self.value = value
        self.ref = ref

    def to_dict(self):
        return {'value': self.value, 'ref': self.ref}


class Insight:
    source: str
    content: Content
    id: int
    type: str
    tagged_users: List[Any]

    def __init__(self, source: str, content: Content, insight_id: int, insight_type: str,
                 tagged_users: List[Any]) -> None:
        self.source = source
        self.content = content
        self.id = insight_id
        self.type = insight_type
        self.tagged_users = tagged_users

    def to_dict(self):
        return {
            'source': self.source,
            'content': self.content.to_dict(),
            'id': self.id,
            'type': self.type,
            'tagged_users': self.tagged_users
        }


class Source:
    model_name: str
    raw_data_infos: List[Any]

    def __init__(self, model_name: str, raw_data_infos: List[Any]) -> None:
        self.model_name = model_name
        self.raw_data_infos = raw_data_infos

    def to_dict(self):
        return {'model_name': self.model_name, 'raw_data_infos': self.raw_data_infos}


class Item:
    general: General
    context: List[ContextElement]
    source: Source
    insights: List[Insight]

    def __init__(self, general: General, context: List[ContextElement], source: Source,
                 insights: List[Insight]) -> None:
        self.general = general
        self.context = context
        self.source = source
        self.insights = insights

    def to_dict(self):
        return {
            'general': self.general.to_dict(),
            'context': [element.to_dict() for element in self.context],
            'source': self.source.to_dict(),
            'insights': [insight.to_dict() for insight in self.insights]
        }


class PipelineItem:
    item: Item

    def __init__(self, item: Item) -> None:
        self.item = item

    def to_dict(self):
        return {'item': self.item.to_dict()}


class ProtocolizedMessage:
    data: PipelineItem
    context: PipelineContext

    def __init__(self, data: PipelineItem, context: PipelineContext) -> None:
        self.data = data
        self.context = context

    def to_dict(self):
        return {
            'data': self.data.to_dict(),
            'context': self.context.to_dict()
        }

    class UUIDEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, UUID):
                return str(obj)
            return super().default(obj)
