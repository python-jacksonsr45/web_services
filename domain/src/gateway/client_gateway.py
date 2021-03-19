from abc import ABC, abstractmethod
from ..request import ClientRequest


class ClientInterface(ABC):
    @classmethod
    @abstractmethod
    def insert_client(cls, request: ClientRequest):
        raise Exception("Method not implemented")
