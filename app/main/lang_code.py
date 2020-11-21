"""
国际化的蓝图 URL  https://dormousehole.readthedocs.io/en/latest/patterns/urlprocessors.html
"""
from flask import g
from . import main  # 包相对导入 https://docs.python.org/zh-cn/3/reference/import.html#package-relative-imports


@main.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)


@main.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')
