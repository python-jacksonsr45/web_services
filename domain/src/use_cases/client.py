from ..presenter import ClientPresenterInterface
from ..gateway import ClientInterface
from ..request import ClientRequest
from ..response import ClientResponse


class Client:
    def __init__(self, client_interface: ClientInterface):
        self.client_interface = client_interface

    def new_user_registration(
        self, request: ClientRequest, presenter: ClientPresenterInterface
    ):
        presenter.present(ClientResponse(self.client_interface.insert_client(request)))
