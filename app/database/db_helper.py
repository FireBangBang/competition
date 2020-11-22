import os
# import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
import xlrd
import xlwt
from structlog import get_logger

from framework import vthread

from app.database.user_model import UserModel
from build import excel_name
from app.constant import const

log = get_logger()  # 日志对象


class Db(object):
    """
    从excel（2020zhiliang.xls）中读取数据放入列表__data中
    用户数据放入列表__users中
    """
    __data = []
    __have_selected = []
    __users = []

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        此处应该通过app.config来构建url。
        Args:
            app: 根据app的配置来初始化
        """
        url_read = r"./app/origin/" + excel_name
        url_write = r"./app/origin/" + "output.xls"
        self.__get_data_from_excel(url_read)
        self.__init_users()
        self.write_to_excel(url_write, "成绩")

        # 数据库初始化
        # self.init_db(app)
        # app.teardown_appcontext(self.close_db)
        # app.cli.add_command(self.init_db_command)

    @vthread.pool(5)  # 在线程数为5的线程池中执行
    @vthread.atom  # 原子操作
    def __get_data_from_excel(self, url):
        with xlrd.open_workbook(url) as xl:
            sheets = xl.sheet_names()
            log.info(sheets)
            for sheet_name in sheets:
                sheet_content = xl.sheet_by_name(sheet_name)
                # 第一行表头不读入
                # self.__data.append([sheet_content.row_values(i + 1)
                #                     for i in range(sheet_content.nrows - 1)])
                table = []
                for i in range(sheet_content.nrows - 1):
                    row_data = []
                    for j in range(sheet_content.ncols):
                        row_data.append(sheet_content.cell(i + 1, j).value)
                        # log.info(sheet_content.cell(i + 1, j).value)
                    table.append(row_data)
                    log.info(row_data)
                self.__data.append(table)

                have_s = []
                self.__have_selected.append(have_s)

            # logger.info(self.__data)
            # current_app.logger.info(self.__data)

    def __init_users(self):
        # self.__user_names = ['资材部', '质量部', '行政部', '组包部', '工程部', 'SMT部', 'HR部']
        self.__user_names = const.USER_NAMES
        for i, name in enumerate(self.__user_names):
            user = UserModel()
            user.user_id = i + 1  # id从1开始递增
            user.user_name = name
            user.rank = i + 1
            self.__users.append(user)
        log.info(user.__dict__.keys())

        log.info("json: ")
        for user in self.__users:
            log.info(list(user.__dict__.values()))
        data = {
            "headers": const.EXCEL_HEADERS,
            "users": [
                list(user.__dict__.values()) for user in self.__users
            ]
        }
        log.info(data, out_of_the_box=True, effort=0)

    # @vthread.pool(5)
    # @vthread.atom
    def fetch_data(self):
        return self.__data

    # @vthread.pool(5)
    # @vthread.atom
    def fetch_users(self):
        users = []
        for user in self.__users:
            u = UserModel()
            u.__dict__ = user.__dict__
            users.append(u)
        length = len(users)
        for i in range(1, length):
            for j in range(0, length-i):
                if users[j].score < users[j+1].score:
                    users[j], users[j+1] = users[j+1], users[j]
        for i, user in enumerate(users):
            user.rank = i + 1

        return users

    def get_one_user(self, name):
        user_names = [user.user_name for user in self.__users]
        p = user_names.index(name)
        return self.__users[p]

    # @vthread.pool(5)
    # @vthread.atom
    def update_users(self, user):
        """
        更新users代码。
        Return: 返回所有用户列表
        """
        cursor = self.__user_names.index(user.user_name)
        self.__users[cursor] = user
        return self.__users

    @vthread.pool(5)
    @vthread.atom
    def write_to_excel(self, url_write, sheet_name):
        wb = xlwt.Workbook()
        ws = wb.add_sheet(sheet_name, True)  # 复写单元格忽略错误
        self.__write_headers(ws)
        for i, user in enumerate(self.__users):
            raw = i + 1
            for j, item in enumerate(list(user.__dict__.values())):
                ws.write(raw, j, item)  # 等同上列注释的部分

        wb.save(url_write)

    def __write_headers(self, sheet):
        # headers = ['序号', '部门', '排名', '得分',
        #           '单选答题', '单选正确', '单选得分',
        #           '多选答题', '多选正确', '多选得分',
        #           '判断答题', '判断正确', '判断得分',
        #           '简答题', '简答正确', '简答得分']
        headers = const.EXCEL_HEADERS
        print(headers)
        for i in range(len(headers)):
            sheet.write(0, i, headers[i])
        log.info(len(self.__users))

    def check_have_been_selected(self, which_sheet, num):
        return num in self.__have_selected[which_sheet]

    def init_db(self, app):
        db = self.get_db(app)

        with app.open_resource(os.path.join(r"./database/" + "schema.sql")) as f:
            # r"./app/database/"
            print(f)
            db.executescript(f.read().decode('utf8'))

    """
    定义一个名为 init-db 命令行，它调用 init_db 函数，并为用户显示一个成功的消息。
    https://dormousehole.readthedocs.io/en/latest/cli.html
    """
    @click.command('init-db')
    @with_appcontext
    def init_db_command(self):
        """Clear the existing data and create new tables."""
        self.init_db(current_app)
        click.echo('Initialized the database.')

    # def get_db(self, app):
    #     if 'db' not in g:
    #         g.db = sqlite3.connect(
    #             current_app.config['DATABASE'],
    #             detect_types=sqlite3.PARSE_DECLTYPES
    #         )
    #         g.db.row_factory = sqlite3.Row

        print(g.db)
        return g.db

    def close_db(self, e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()


db = Db()  # 单例模式
