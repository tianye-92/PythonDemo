import sys


def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
# 获取sum_and_avg函数返回的多个值，多个返回值被封装成元组
tp = sum_and_avg(my_list)  # ①
print(tp)

s, avg = sum_and_avg(my_list)  # ②
print(s)
print(avg)


class Bird:
    # classmethod修饰的方法是类方法
    @classmethod
    def fly(cls):
        cls.testDemo('hello')
        print('类方法fly: ', cls)

    # staticmethod修饰的方法是静态方法
    @staticmethod
    def info(p):
        print('静态方法info: ', p)

    def testDemo(self):
        print(self, 'testDemo!')


Bird.info('dsa')

Bird.fly()

b = Bird()

b.fly()

import Item

print(Item.__doc__)

print('环境变量：', sys.path)

__all__ = {}

