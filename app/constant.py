# -*- coding: utf-8 -*-
# python 3.x


class Const(object):
    """
    定义一个常量类实现常量的功能。

    该类定义了一个方法__setattr()__。 通过调用类自带的字典__dict__,
    判断定义的常量是否包含在字典中。如果字典中包含此变量，将抛出异常，
    否则，给新创建的常量赋值。如果常量名不是全大写，将抛出异常。

    Raise:
        ConstError: 常量已经存在的错误。
        ConstCaseError: 常量书写不是全大写的错误。
    """

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            # 存在性验证
            raise self.ConstError("Can't rebind const (%s)" % name)
        if not name.isupper():
            # 语法规范验证
            raise self.ConstCaseError("Const variable must be combined "
                                      "with upper letters:'%s'" % name)
        self.__dict__[name] = value


"""
若注册到sys中，可以在其他module中定义常量，例如：
import const
const.PI = 3.14159265358
但最优雅的方式是一个app中把所有常量集中定义。
"""
# import sys
# sys.modules[__name__] = Const()

const = Const()

const.SLOGAN = r"质量第一 客户至上"
const.USER_NAMES = ('资材部', '质量部', '行政部', '组包部', '工程部', 'SMT部', 'HR部')
const.EXCEL_HEADERS = (
    '序号', '部门', '得分', '排名',
    '单选答题', '单选正确', '单选得分',
    '多选答题', '多选正确', '多选得分',
    '判断答题', '判断正确', '判断得分',
    '简答题', '简答正确', '简答得分'
)
