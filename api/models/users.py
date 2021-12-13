from sqlalchemy import Column, Integer, String
from typing import Union
import bcrypt

from api.database import Base

class User(Base):
    """[summary]

    Args:
        Base (any): [description]

    Returns:
        [type]: [description]
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), unique=False, nullable=False)

    def __init__(self, username: str = "", password: str = ""):
        """[summary]

        Args:
            username (str, optional): [description]. Defaults to "".
            password (str, optional): [description]. Defaults to "".
        """
        self.username = username
        self.password = password

    def login(username: str, password: str) -> Union[User, bool]:
        """[summary]

        Args:
            username (str): [description]
            password (str): [description]

        Returns:
            Union[User, bool]: [description]
        """
        user = User.query.filter_by(username=username).first()

        if user != None and bcrypt.checkpw(password.encode(), user.password):
            return user

        return False

    def register():

