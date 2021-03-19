import uuid
from datetime import datetime
from ..entity import UserEntity, AddressEntity, ProfileEntity


class ClientEntity:
    def __init__(
        self,
        client_id: str = None,
        user: UserEntity = None,
        profile: ProfileEntity = None,
        address: AddressEntity = None,
        created_at: datetime = None,
    ):
        if client_id is not None:
            self.client_id = client_id
        else:
            self.client_id = str(uuid.uuid4())
        self.user = user
        self.profile = profile
        self.address = address
        if not created_at:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        self.updated_at = datetime.now()

    def get_user(self) -> UserEntity:
        return self.user

    def get_profile(self) -> ProfileEntity:
        return self.profile

    def get_address(self) -> AddressEntity:
        return self.address

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.updated_at
