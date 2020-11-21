from app.api.code import ResponseCode, ResponseMessage


class ResMsg(object):
    """
    封装响应文本
    """

    def __init__(self, data=None, code=ResponseCode.SUCCESS,
                 msg=ResponseMessage.SUCCESS):
        self.__data = data
        self.__msg = msg
        self.__code = code

    def update(self, code=None, data=None, msg=None):
        """
        更新默认响应文本
        :param code:响应状态码
        :param data: 响应数据
        :param msg: 响应消息
        :return:
        """
        if not code:
            self.__code = code
        if not data:
            self.__data = data
        if not msg:
            self.__msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if not name and not value:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["data"] = body.pop("__data")
        body["msg"] = body.pop("__msg")
        body["code"] = body.pop("__code")
        return body
