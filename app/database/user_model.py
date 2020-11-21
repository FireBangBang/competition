class UserModel:

    err_numbers = 'score must be numbers!'

    def __init__(self):
        self.__user_id = 1
        self.__user_name = ''
        self.__score = 100
        self.__rank = 0
        self.__single_count = 0
        self.__single_correct = 0
        self.__single_score = 0
        self.__multiple_count = 0
        self.__multiple_correct = 0
        self.__multiple_score = 0
        self.__deter_count = 0
        self.__deter_corr = 0
        self.__deter_score = 0
        self.__resp_count = 0
        self.__resp_corr = 0
        self.__resp_score = 0

    def __check_num(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(self.err_numbers)

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__check_num(score)
        self.__score = score

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__check_num(rank)
        self.__rank = rank

    @property
    def single_count(self):
        """
        单选题数量
        :return:
        """
        return self.__single_count

    @single_count.setter
    def single_count(self, single_count):
        self.__check_num(single_count)
        self.__single_count = single_count

    @property
    def single_correct(self):
        """
        单选题正确数量
        :return:
        """
        return self.__single_correct

    @single_correct.setter
    def single_correct(self, single_correct):
        self.__check_num(single_correct)
        self.__single_correct = single_correct

    @property
    def single_score(self):
        return self.__single_score

    @single_score.setter
    def single_score(self, single_score):
        self.__check_num(single_score)
        self.__single_score = single_score

    @property
    def multiple_count(self):
        """
        简答题数量
        :return:
        """
        return self.__multiple_count

    @multiple_count.setter
    def multiple_count(self, multiple_count):
        self.__check_num(multiple_count)
        self.__multiple_count = multiple_count

    @property
    def multiple_correct(self):
        return self.__multiple_correct

    @multiple_correct.setter
    def multiple_correct(self, multiple_correct):
        self.__check_num(multiple_correct)
        self.__multiple_correct = multiple_correct

    @property
    def multiple_score(self):
        return self.__multiple_score

    @multiple_score.setter
    def multiple_score(self, multiple_score):
        self.__check_num(multiple_score)
        self.__multiple_score = multiple_score

    @property
    def deter_count(self):
        """
        判断题数量
        :return:
        """
        return self.__deter_count

    @deter_count.setter
    def deter_count(self, deter_count):
        self.__check_num(deter_count)
        self.__deter_count = deter_count

    @property
    def deter_corr(self):
        return self.__deter_corr

    @deter_corr.setter
    def deter_corr(self, deter_corr):
        self.__check_num(deter_corr)
        self.__deter_corr = deter_corr

    @property
    def deter_score(self):
        return self.__deter_score

    @deter_score.setter
    def deter_score(self, deter_score):
        self.__check_num(deter_score)
        self.__deter_score = deter_score

    @property
    def resp_count(self):
        """
        简答题数量
        :return:
        """
        return self.__resp_count

    @resp_count.setter
    def resp_count(self, resp_count):
        self.__check_num(resp_count)
        self.__resp_count = resp_count

    @property
    def resp_corr(self):
        return self.__resp_corr

    @resp_corr.setter
    def resp_corr(self, resp_corr):
        self.__check_num(resp_corr)
        self.__resp_corr = resp_corr

    @property
    def resp_score(self):
        return self.__resp_score

    @resp_score.setter
    def resp_score(self, resp_score):
        self.__check_num(resp_score)
        self.__resp_score = resp_score


def update(user, dic):
    user.user_id = dic["user_id"]
    user.user_name = dic["user_name"]
    user.score = dic["score"]
    user.rank = dic["rank"]
    user.single_count = dic["single_count"]
    user.single_correct = dic["single_correct"]
    user.single_score = dic["single_score"]
    user.multiple_count = dic["multiple_count"]
    user.multiple_correct = dic["multiple_correct"]
    user.multiple_score = dic["multiple_score"]
    user.deter_count = dic["deter_count"]
    user.deter_corr = dic["deter_corr"]
    user.deter_score = dic["deter_score"]
    user.resp_count = dic["resp_count"]
    user.resp_corr = dic["resp_corr"]
    user.resp_score = dic["resp_score"]
    return user

# if __name__ == '__main__':
#     cls = UserModel()
#     print(cls.__dict__)
