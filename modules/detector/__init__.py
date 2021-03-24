#################################
# Date: 2021/03/24
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 管理modules下哪些包可以暴露
#        仅暴露公共使用的API，modules
#        内部使用的都封锁在modules内部
#################################
# -*- coding: utf-8 -*-

from .recognize import recognizeFace
from .detect import detectFace, detectFaceKeyPoint

__all__ = [
    recognizeFace,
    detectFace,
    detectFaceKeyPoint
]