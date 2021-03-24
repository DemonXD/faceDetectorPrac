#################################
# Date: 2021/03/24
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 选择器，按照输入的类型选择
#        相应的处理器
#################################
# -*- coding: utf-8 -*-

import functools

# def selector(func):
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapped

class Selector:

    def __init__(self, args):
        print(args.target)