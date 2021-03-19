from ..entity import UserEntity, AddressEntity, ProfileEntity
from ..request import ClientRequest


class ClientResponse:
    def __init__(self, request: ClientRequest):
        self.user = request.user
        self.profile = request.profile
        self.address = request.address

    def get_user(self) -> UserEntity:
        return self.user

    def get_profile(self) -> ProfileEntity:
        return self.profile

    def get_address(self) -> AddressEntity:
        return self.address
