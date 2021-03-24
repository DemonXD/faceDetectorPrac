#################################
# Date: 2021/03/24
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 人脸检测接口
#################################
# -*- coding: utf-8 -*-
import cv2
from .detector import Detector

def detectFace(img):
    """[summary]

    Args:
        img ([opencv img]): [opencv 图片格式]
    
    图片或从摄像头读取，或从文件，或者视频读取，都为opencv的帧图像
    """
    # 分离三色通道, 从BGR->RGB
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    # 返回人脸检测的结果
    dets = Detector.detector(img2, 1)
    if len(dets == 0): return None
    for index, face in enumerate(dets):
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
    return img

def detectFaceKeyPoint(img):
    """[summary]

    Args:
        img ([opencv img]): [人脸关键点检测]
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = Detector.detector(gray, 1)
    for face in dets:
        shape = Detector.detectorKey(img, face)
        for pt in shape.parts():
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
    return img