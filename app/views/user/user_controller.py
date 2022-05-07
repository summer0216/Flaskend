from flask import Blueprint, jsonify
from werkzeug.debug import console

from .user_model import User
from .user_service import UserService

user = Blueprint('user', __name__, url_prefix='/user/')


@user.route('/', methods=['GET'])
def user_list():
    users = User.query.all()
    console.log(users)
    return users


# 用户增加


# 用户删除

# 用户查询

# 用户修改
