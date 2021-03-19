from abc import ABC, abstractmethod
from ..response import ClientResponse


class ClientPresenterInterface(ABC):
    @abstractmethod
    def present(self, response: ClientResponse):
        raise Exception("Method not implemented")
