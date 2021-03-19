from datetime import datetime
from ..entity import UserEntity, AddressEntity, ProfileEntity
from ..request import ClientRequest


class ClientResponse:
    def __init__(self, request: ClientRequest):
        self.client_id = request.client_id
        self.user = request.user
        self.profile = request.profile
        self.address = request.address
        self.created_at = request.created_at
        self.updated_at = request.updated_at

    def get_id(self):
        return self.client_id

    def get_user(self) -> UserEntity:
        return self.user

    def get_profile(self) -> ProfileEntity:
        return self.profile

    def get_address(self) -> AddressEntity:
        return self.address

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.created_at
