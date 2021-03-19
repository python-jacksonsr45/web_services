from ..presenter import ClientPresenterInterface
from ..gateway import ClientInterface
from ..request import ClientRequest
from ..response import ClientResponse


class Client:
    def __init__(self, client_interface: ClientInterface):
        self.client_interface = client_interface

    def new_client_registration(
        self, request: ClientRequest, presenter: ClientPresenterInterface
    ):
        presenter.present(ClientResponse(self.client_interface.insert_client(request)))

    def update_client_registration(
        self, request: ClientRequest, presenter: ClientPresenterInterface
    ):
        presenter.present(ClientResponse(self.client_interface.update_client(request)))

    def find_client_registration_by_id(
        self, client_id: str, presenter: ClientPresenterInterface
    ):
        presenter.present(
            ClientResponse(self.client_interface.find_client_by_id(client_id))
        )
