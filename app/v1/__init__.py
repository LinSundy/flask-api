# 此处需要把红图都关联到蓝图
from flask import Blueprint
from app.v1 import author, book


def create_blueprint_v1():
    v1_blueprint = Blueprint('v1_blueprint', __name__)  # 蓝图的实例对象
    # 这个过程中需要实现红图的关联
    author.api.register(v1_blueprint)
    # book.api.register(v1_blueprint)
    return v1_blueprint
