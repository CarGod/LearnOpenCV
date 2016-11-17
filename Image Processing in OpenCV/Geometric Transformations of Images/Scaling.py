#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-17 20:25:09
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    放大或缩小图像
"""
import numpy as np
import cv2


img = cv2.imread('../../GuiFeaturesinOpenCV/temp.jpg')

"""
    图片，
    设定宽度(接受的是一个元组)， 
    方法或缩小比例(fx, fy)，
    插值方法：  
        cv2.INTER_AREA  双线性插值 (缺省使用)
        cv2.INTER_CUBIC  使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..
        cv2.INTER_LINEAR  立方插值.
"""
res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
height, width = img.shape[:2]
res2 = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
