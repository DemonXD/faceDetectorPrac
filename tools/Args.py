#################################
# Date: 2021/03/24
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 初始化命令行参数
#################################
# -*- coding: utf-8 -*-

import argparse

def initArges():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target",
        help="target => [*.jpg|*.png|folder|*.mp4]"
    )
    args = parser.parse_args()
    return args