import time


def datetime_creator():
    """
    返回标准格式的datetime
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def date_creator():
    """
    返回标准格式的日期
    :return:
    """
    return time.strftime("%Y-%m-%d", time.localtime())


def time_creator():
    """
    返回标准格式的时间
    :return:
    """
    return time.strftime("%H:%M:%S", time.localtime())
