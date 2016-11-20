#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 22:55:49
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    输入图像和输入图像的关闭之间的差异
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('j.png', 0)
kernel = np.ones((9, 9), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(blackhat), plt.title('Black Hat')
plt.show()
