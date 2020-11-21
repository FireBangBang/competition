from flask import Blueprint

# 两个参数分别指定蓝本的名字、蓝本所在的包或模块  国际化的 蓝本url用注释这句
# main = Blueprint('main', __name__, url_prefix='/<lang_code>')
main = Blueprint('main', __name__)


# 导入路由模块，将其和蓝本关联起来
# 在蓝本的末尾导入在两个模块里还要导入蓝本，防止循环导入依赖
from app.main import views
