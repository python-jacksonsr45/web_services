from faker import Faker
import uuid
from domain.src.request import ClientRequest
from domain.src.response import ClientResponse
from domain.src.use_cases import Client
from domain.src.presenter import ClientPresenterInterface
from domain.src.gateway import ClientInterface
from domain.src.entity import UserEntity, ProfileEntity, AddressEntity, ClientEntity


class ClientPresenter(ClientPresenterInterface):
    def __init__(self):
        self.client_user_view = None

    def present(self, response: ClientResponse):
        self.client_user_view = ClientEntity(
            client_id=response.client_id,
            user=response.user,
            address=response.address,
            profile=response.profile,
        )

    def get_client_view_model(self) -> ClientEntity:
        return self.client_user_view


presenter: ClientPresenterInterface = ClientPresenter()
faker = Faker()


class ClientRepository(ClientInterface):
    @classmethod
    def insert_client(cls, request: ClientRequest):
        return ClientEntity(
            user=request.user, address=request.address, profile=request.profile
        )

    @classmethod
    def update_client(cls, request: ClientRequest):
        return ClientEntity(
            user=request.user, address=request.address, profile=request.profile
        )

    @classmethod
    def find_client_by_id(cls, client_id):
        request = presenter.get_client_view_model()
        return ClientEntity(
            client_id=client_id,
            user=request.user,
            address=request.address,
            profile=request.profile,
        )


client_interface: ClientInterface = ClientRepository
client = Client(client_interface)

username = "user_test"
password = faker.password()
email = faker.email()
user = UserEntity(username=username, password=password, email=email)

name = "user"
last_name = "test"
document_id = "123456789"
phone = "15321654"
mobile_phone = "4561235465"
profile = ProfileEntity(
    name=name,
    last_name=last_name,
    phone=phone,
    mobile_phone=mobile_phone,
    document_id=document_id,
)

country = "Brasil"
state = "Parana"
zip_code = "86400000"
neighborhood = "Bairro de Teste"
street = "Rua de Teste"
number = "1234"
address = AddressEntity(
    country=country,
    state=state,
    zip_code=zip_code,
    neighborhood=neighborhood,
    street=street,
    number=number,
)

client_request = ClientRequest(user=user, profile=profile, address=address)


def test_new_client_registration():
    """ Should be creating a new client and verify data """

    client.new_client_registration(client_request, presenter)

    new_client = presenter.get_client_view_model()

    assert new_client.client_id is not None
    assert new_client.user == user
    assert new_client.address == address
    assert new_client.profile == profile
    assert new_client.created_at is not None
    assert new_client.updated_at is not None


def test_update_client_registration():
    """ Should be updating client registration and compare result """

    client_request.user.username = "test123456"
    client.update_client_registration(client_request, presenter)

    new_client = presenter.get_client_view_model()

    assert new_client.user.username == "test123456"


def test_find_client_registration_by_id():
    """ Should be find client registration by id and compare result """

    client_id = str(uuid.uuid4())
    client_request.client_id = client_id
    client.new_client_registration(client_request, presenter)

    client.find_client_registration_by_id(client_id=client_id, presenter=presenter)

    result = presenter.get_client_view_model()

    assert result.client_id == client_id
