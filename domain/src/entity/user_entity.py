import uuid
from datetime import datetime


class UserEntity:
    def __init__(
        self,
        user_id: str = None,
        username: str = None,
        password: str = None,
        email: str = None,
        created_at: datetime = None,
    ):
        if not user_id:
            self.id = str(uuid.uuid4())
        else:
            self.id = user_id
        self.username = username
        self.password = password
        self.email = email
        if not created_at:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        self.updated_at = datetime.now()

    def get_id(self) -> str:
        return self.id

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_email(self) -> str:
        return self.email

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.updated_at
