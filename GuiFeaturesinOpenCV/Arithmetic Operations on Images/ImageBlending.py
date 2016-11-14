#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-14 21:29:56
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


img1 = cv2.imread('m1.png')
img2 = cv2.imread('opencv-logo.png')

print(img1)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

# 两个图片的类型，行，宽，通道，必须一致，否则报错。
"""
    第一个参数：
        第一张图片
    第二个参数：
        第一张图片的透明度，数值越小，越透明。
        1为不透明，0为不可见。
    第三个参数：
        第二张图片
    第四个参数：
        第二张图片的透明度
    第五个参数：
        图片合成后的曝光程度，数值越大图片越亮。
"""
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
