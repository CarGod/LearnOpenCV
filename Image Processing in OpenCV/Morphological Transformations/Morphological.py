#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 22:45:58
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    形态梯度
    看起来像是把图像转换成轮廓
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(gradient), plt.title('Gradient')
plt.show()
