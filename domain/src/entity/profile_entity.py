import uuid
from datetime import datetime


class ProfileEntity:
    def __init__(
        self,
        profile_id: str = None,
        name: str = None,
        last_name: str = None,
        phone: str = None,
        mobile_phone: str = None,
        created_at: str = None,
    ):
        if not profile_id:
            self.id = str(uuid.uuid4())
        else:
            self.id = profile_id
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.mobile_phone = mobile_phone
        if not created_at:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        self.updated_at = datetime.now()

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_last_name(self) -> str:
        return self.last_name

    def get_phone(self) -> str:
        return self.phone

    def get_mobile_phone(self) -> str:
        return self.mobile_phone

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.updated_at
