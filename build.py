import os

basedir = os.path.abspath(os.path.dirname(__file__))
excel_name = '2020zhiliang.xls'


# https://dormousehole.readthedocs.io/en/latest/config.html#config-dev-prod
class Config(object):
    # 用于建立动态token令牌，用于验证Form表单提交，
    # 免受跨站请求伪造（Cross-Site Request Forgery，CSRF）攻击
    SECRET_KEY = (os.environ.get('SECRET_KEY')
                  or b"\x96H\xe8'(\x10\xa4\xb5\xd1\x80O\x1c\x81=\x82\xd6")
    EXPLAIN_TEMPLATE_LOADING = False  # Flask 会打印出定位模板的步骤，方便调试。


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    url = r"./app/origin/" + excel_name
    DATABASE = os.path.join(r"./app/database/", 'competition_dev.sqlite')


# 测试环境的配置
class TestingConfig(Config):
    TESTING = True
    url = r"./app/origin/" + excel_name
    DATABASE = os.path.join(basedir, 'competition_test.sqlite')


# 生产环境的配置
class ProductionConfig(Config):
    url = r"./app/origin/" + excel_name
    DATABASE = os.path.join(basedir, 'competition.sqlite')
    EXPLAIN_TEMPLATE_LOADING = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
