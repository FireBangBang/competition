from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask import Blueprint
from flask_wtf.csrf import CSRFProtect
import logging
from logging.config import dictConfig

from structlog import get_logger

from build import config
import app.constant  # 初始化全局常量
from app.database.db_helper import db

bootstrap = Bootstrap()
# 能够让所有的视图函数受到 CSRF 保护
# http://www.pythondoc.com/flask-wtf/csrf.html
csrf = CSRFProtect()
# db = Db()

login_manager = LoginManager()
# 设置安全等级，防止用户回话被篡改（None,'basic','strong'）
# 设置为strong Flask-Login会记住客户端ip和浏览器的用户代理信息，如果发现异动就登出用户
login_manager.session_protection = 'strong'
# 设置登录页面的端点，
login_manager.login_view = 'auth.login'
# 设置快闪消息，使用@login_required装饰器的路由要用到
login_manager.login_message = '该操作需要先登录账号'

"""
使用 dictConfig() 来创建一个类似于 Flask 缺 省配置的日志记录配置。
来源frask官方文档 https://dormousehole.readthedocs.io/en/latest/logging.html
"""
logging_conf = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}


def create_app(config_name):
    # 通过使用配置对象来根据关联文件名从文件中载入配置，那么就可以通过改
    # 变与实例路径相关联的文件名来按需要载入不同配置。在配置文件中的关联路径的行
    # 为可以在 “关联到应用的根路径”（缺省的）和 “关联到实例文件夹”之间变换，
    # 具体通过应用构建函数中的 instance_relative_config 来实现
    # https://dormousehole.readthedocs.io/en/latest/config.html#instance-folders
    app = Flask(__name__, instance_relative_config=True)

    logging.config.dictConfig(logging_conf)
    # 导致指定的配置对象
    app.config.from_object(config[config_name])
    print("app.config")
    print(app.config)
    get_logger(app.config.from_object(config[config_name]))

    # 初始化扩展
    bootstrap.init_app(app)
    csrf.init_app(app)
    with app.app_context():
        db.init_app(app)

    # register_api(app, router_list)
    register_router(app)

    return app


def register_router(app):
    # 一个 yourapplication/admin 文件夹中的蓝本并且你想要渲染 'admin/index.html' 模板，
    # 且你已经提供了 templates 作为 template_folder ，你需要这样创建文件:
    # yourapplication/admin/templates/admin/index.html
    # 所以使用url_prefix注册后，蓝本中定义的所有路由都会加上指定前缀，/login --> /main/login
    # https://dormousehole.readthedocs.io/en/latest/blueprints.html#id9
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.minor import minor as minor_blueprint
    app.register_blueprint(minor_blueprint)
    # from app.database import database as db_blueprint
    # app.register_blueprint(db_blueprint)


# def register_api(app, routers):
#     for router_api in routers:
#         if isinstance(router_api, Blueprint):
#             # 一个 yourapplication/admin 文件夹中的蓝本并且你想要渲染 'admin/index.html' 模板，
#             # 且你已经提供了 templates 作为 template_folder ，你需要这样创建文件:
#             # yourapplication/admin/templates/admin/index.html
#             # 所以使用url_prefix注册后，蓝本中定义的所有路由都会加上指定前缀，/login --> /main/login
#             # https://dormousehole.readthedocs.io/en/latest/blueprints.html#id9
#             app.register_blueprint(router_api)
#         else:
#             try:
#                 endpoint = router_api.__name__
#                 view_func = router_api.as_view(endpoint)
#                 # url默认为类名小写
#                 url = '/{}/'.format(router_api.__name__.lower())
#                 if 'GET' in router_api.__methods__:
#                     app.add_url_rule(url, defaults={'key': None}, view_func=view_func, methods=['GET', ])
#                     app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['GET', ])
#                 if 'POST' in router_api.__methods__:
#                     app.add_url_rule(url, view_func=view_func, methods=['POST', ])
#                 if 'PUT' in router_api.__methods__:
#                     app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['PUT', ])
#                 if 'DELETE' in router_api.__methods__:
#                     app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['DELETE', ])
#             except Exception as e:
#                 raise ValueError(e)
