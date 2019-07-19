# coding:utf8
"""
redis在Python中的操作
"""
from redis import StrictRedis


class RedisTest(object):
    def __init__(self):
        self.sr = StrictRedis(host="10.61.121.80", port=6379)

    def add_data(self):
        key = "name"
        value = "li"
        self.sr.set(key, value)


if __name__ == '__main__':
    try:
        rt = RedisTest()
        print(rt.add_data())
    except Exception as e:
        print(e)
