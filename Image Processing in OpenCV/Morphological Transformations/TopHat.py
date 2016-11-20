#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 22:49:23
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    输入图像和图像开口之间的差异
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('j.png', 0)
kernel = np.ones((9, 9), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(tophat), plt.title('Top Hat')
plt.show()
