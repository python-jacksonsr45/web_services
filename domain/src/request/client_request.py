from datetime import datetime
from ..entity import UserEntity, AddressEntity, ProfileEntity


class ClientRequest:
    def __init__(
        self,
        client_id: str = None,
        user: UserEntity = None,
        profile: ProfileEntity = None,
        address: AddressEntity = None,
        created_at: datetime = None,
        updated_at: datetime = None,
    ):
        self.client_id = client_id
        self.user = user
        self.profile = profile
        self.address = address
        self.created_at = created_at
        self.updated_at = updated_at

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
