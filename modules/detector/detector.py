#################################
# Date: 2021/03/24
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 
#################################
# -*- coding: utf-8 -*-
from config import PREDICTOR_FILE
import dlib

class Detector:
    detector = dlib.get_frontal_face_detector()
    detectorKey = dlib.shape_predictor(
        PREDICTOR_FILE
    ) # 获取人脸分类器