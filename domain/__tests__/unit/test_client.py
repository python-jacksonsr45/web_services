from faker import Faker
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
            user=response.user, address=response.address, profile=response.profile
        )

    def get_client_view_model(self) -> ClientEntity:
        return self.client_user_view


class ClientRepository(ClientInterface):
    @classmethod
    def insert_client(cls, request: ClientRequest):
        return ClientEntity(
            user=request.user, address=request.address, profile=request.profile
        )


client_interface: ClientInterface = ClientRepository
client = Client(client_interface)
presenter: ClientPresenterInterface = ClientPresenter()
faker = Faker()


def test_new_user_registration():
    username = "user_test"
    password = faker.password()
    email = faker.email()
    user = UserEntity(username=username, password=password, email=email)

    name = "user"
    last_name = "test"
    phone = "15321654"
    mobile_phone = "4561235465"
    profile = ProfileEntity(
        name=name, last_name=last_name, phone=phone, mobile_phone=mobile_phone
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

    client.new_user_registration(client_request, presenter)

    new_client = presenter.get_client_view_model()

    assert new_client.user.username == username
    assert new_client.user.password == password
    assert new_client.user.email == email
    assert new_client.profile.name == name
    assert new_client.profile.last_name == last_name
    assert new_client.profile.phone == phone
    assert new_client.profile.mobile_phone == mobile_phone
    assert new_client.address.country == country
    assert new_client.address.state == state
    assert new_client.address.zip_code == zip_code
    assert new_client.address.neighborhood == neighborhood
    assert new_client.address.street == street
    assert new_client.address.number == number
