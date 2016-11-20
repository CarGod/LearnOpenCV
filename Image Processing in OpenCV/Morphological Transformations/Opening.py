#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 21:40:40
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    开放
    开放是侵蚀的另一个说法，在去除噪声的领域很好用。
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('opening.png', 0)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 1)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(opening), plt.title('Opening')
plt.show()