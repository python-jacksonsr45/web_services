import uuid
from datetime import datetime


class AddressEntity:
    def __init__(
        self,
        address_id: str = None,
        country: str = None,
        state: str = None,
        zip_code: str = None,
        neighborhood: str = None,
        street: str = None,
        number: str = None,
        created_at: str = None,
    ):
        if not address_id:
            self.id = str(uuid.uuid4())
        else:
            self.id = address_id
        self.country = country
        self.state = state
        self.zip_code = zip_code
        self.neighborhood = neighborhood
        self.street = street
        self.number = number
        if not created_at:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        self.updated_at = datetime.now()

    def get_id(self) -> str:
        return self.id

    def get_country(self) -> str:
        return self.country

    def get_state(self) -> str:
        return self.state

    def get_zip_code(self) -> str:
        return self.zip_code

    def get_neighborhood(self) -> str:
        return self.neighborhood

    def get_street(self) -> str:
        return self.street

    def get_number(self) -> str:
        return self.number

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.updated_at
