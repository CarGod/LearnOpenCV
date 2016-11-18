#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-17 21:04:54
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    移动，拉伸图像
"""
import numpy as np
import cv2


img = cv2.imread('../../GuiFeaturesinOpenCV/temp.jpg')
rows, cols, _ = img.shape

"""
    宽，图片右下角向右拉扯的程度，图片左上角的点距离左边缘的距离
    图片右下角向下拉扯的程度，高，图片左上角的点距离上边缘的距离
"""
M = np.float32([[1,0,100], [0,1,50]])


"""
    输入图像
    转换矩阵
    第三个参数是一个元组，接收图像的像素列和行
    width =列数，height =行数
"""
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
