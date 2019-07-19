# coding:utf8
"""
redis在Python中的操作
"""
from redis import StrictRedis


class RedisTest(object):
    def __init__(self):
        self.sr = StrictRedis(host="10.61.121.80", port=6379)

    def add_data(self, key, value):
        """
        redis字符串类型添加方法
        """
        return self.sr.set(key, value)

    def get_data(self, key):
        return self.sr.keys(key)

    def delete_data(self, key):
        return self.sr.delete(key)


if __name__ == '__main__':
    try:
        rt = RedisTest()
        a = 'name'
        b = 'Jack'
        rt.add_data(a, b)
        name = 'name'
        print(rt.get_data(name))
        print(rt.delete_data(name))
    except Exception as e:
        print(e)
