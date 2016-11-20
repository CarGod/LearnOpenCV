#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 19:03:18
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    中间模糊
    对付胡椒粉一样的密密麻麻全是噪点的图像非常好用
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('serrated.png')

"""
    参数一：接收的图像
    参数二：模糊程度
"""
median_blur = cv2.medianBlur(img, 5)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median_blur), plt.title('Median Blur')
plt.xticks([]), plt.yticks([])
plt.show()
