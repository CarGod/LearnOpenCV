#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 21:54:34
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    关闭和开放是相反的，在去除图像里面的小黑点非常有效。
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('closing.png', 0)
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(closing), plt.title('Closing')
plt.show()
