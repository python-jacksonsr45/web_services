from ..entity import UserEntity, AddressEntity, ProfileEntity


class ClientRequest:
    def __init__(
        self,
        user: UserEntity = None,
        profile: ProfileEntity = None,
        address: AddressEntity = None,
    ):
        self.user = user
        self.profile = profile
        self.address = address

    def get_user(self) -> UserEntity:
        return self.user

    def get_profile(self) -> ProfileEntity:
        return self.profile

    def get_address(self) -> AddressEntity:
        return self.address
