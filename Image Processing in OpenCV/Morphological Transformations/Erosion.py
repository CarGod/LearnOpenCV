#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 20:52:56
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    侵蚀图像
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
"""
    iterations 代表重复次数
"""
erosin = cv2.erode(img, kernel, iterations = 1)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(erosin), plt.title('Erosin')
plt.xticks([]), plt.yticks([])
plt.show()
