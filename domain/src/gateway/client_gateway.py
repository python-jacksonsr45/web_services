from abc import ABC, abstractmethod
from ..request import ClientRequest


class ClientInterface(ABC):
    @classmethod
    @abstractmethod
    def insert_client(cls, request: ClientRequest):
        raise Exception("Method not implemented")

    @classmethod
    @abstractmethod
    def update_client(cls, request: ClientRequest):
        raise Exception("Method not implemented")

    @classmethod
    @abstractmethod
    def find_client_by_id(cls, client_id):
        raise Exception("Method not implemented")
