#################################
# Date: 2021/03/24
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 
#################################
# -*- coding: utf-8 -*-
from tools import initArges
from modules.selector import Selector
from modules.detector import (
    detectFace,
    detectFaceKeyPoint,
    recognizeFace
)


def main(selector):
    pass


if __name__ == "__main__":
    try:
        args = initArges()
        main(Selector(args))
    except KeyboardInterrupt:
        pass