import os
from .user_model import User


class UserService(User):
    def __init__(self, **kwargs):

        super(UserService, self).__init__(**kwargs)

