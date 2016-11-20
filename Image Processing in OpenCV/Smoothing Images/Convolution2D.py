#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-19 12:08:01
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    过滤器，过滤模糊图像。
    可以有效的去除图像中的噪点和一些高频的内容。
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('serrated.png')

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
"""
    图像周围的标尺，接收一个list，如：[0,10,200,300]
    如果为[]则不显示标尺，默认会显示0,100,200这样每隔100的标尺。
"""
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()