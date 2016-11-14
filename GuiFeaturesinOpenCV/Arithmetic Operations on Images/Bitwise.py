#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-14 22:14:07
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


img1 = cv2.imread('temp.jpg')
img2 = cv2.imread('opencv-logo.png')

# 得到图片的行和列，以及它的通道数
rows, cols, channels = img2.shape
print(img2.shape)

"""
    读取坐标一般都是横坐标在前，竖坐标在后，正好相反。
    [竖线第一个点:竖线第二个点, 横线第一个点:横线第二个点]
    这里是读取img1的，img2的大小区域，从左上角开始
"""
roi = img1[0:rows, 0:cols]

# 设置为灰度
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# cv2的饱和运算加法
dst = cv2.add(img1_bg, img2_fg)
print(dst)

# img1的img2的行和列大小的区域等于dst。
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
