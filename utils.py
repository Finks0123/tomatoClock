# coding:utf-8
"""
@author:Finks
@time:2022/6/23 15:10

"""
import sys
import os
import random
import itertools

# if hasattr(sys,  "_MEIPASS"):
#     app_path = os.path.join(sys._MEIPASS)
# else:
# app_path = os.path.dirname(os.path.abspath(__file__))

# import sys
# import os


if getattr(sys, 'frozen', False): #是否Bundle Resource
    app_path = sys._MEIPASS
else:
    app_path = os.path.dirname(os.path.abspath(__file__))





def get_iter(name):
    """
    get icon path
    :param name:
    :return: return a iter
    """
    dir_ = os.path.join(app_path, 'source', name)
    path_list = [os.path.join(dir_, i) for i in os.listdir(dir_)]
    img_iter = itertools.cycle(path_list)
    return img_iter


def rand_a_name():
    """
    get a name
    :return: str
    """
    dir_ = os.path.join(app_path, 'source')
    return random.choice(os.listdir(dir_))


if __name__ == '__main__':
    print(rand_a_name())