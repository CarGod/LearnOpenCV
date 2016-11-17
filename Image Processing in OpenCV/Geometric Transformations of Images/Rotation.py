#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-17 21:39:21
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    旋转图像
"""
import numpy as np
import cv2


img = cv2.imread('../../GuiFeaturesinOpenCV/temp.jpg')
rows, cols, _ = img.shape

"""
    第一个参数接收一个元组：
        以这个点作为圆心逆时针旋转
    第二个参数是旋转多少度
    第三个参数是缩放比例
"""
M = cv2.getRotationMatrix2D((cols/2, rows/2), 10, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Rotation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
