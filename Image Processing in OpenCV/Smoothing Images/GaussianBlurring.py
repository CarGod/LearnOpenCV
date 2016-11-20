#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 18:16:30
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    高斯模糊
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('serrated.png')

"""
    参数一：接收的图像
    参数二三：内核的宽和高
    参数三四：x和y方向的标准偏差，如果指定x则y等于x
        或只写一个参数三，参数四会默认等于参数三
        如果为0，则是从内核大小来计算
"""
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0, 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(gaussian_blur), plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()
