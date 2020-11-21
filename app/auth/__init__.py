from flask import Blueprint

# 两个参数分别指定蓝本的名字、蓝本所在的包或模块  国际化的 蓝本url用注释这句
# auth = Blueprint('auth', __name__, url_prefix='/<lang_code>')
auth = Blueprint('auth', __name__)

from app.auth import views
