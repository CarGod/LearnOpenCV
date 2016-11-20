#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 17:23:08
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    图像模糊，图像平滑
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('serrated.png')

"""
    图像左右和上下模糊的程度
    两个数值如果不一样大，就会造成图像上下
    或者左右抖动，看起来会让人发晕。
"""
blur = cv2.blur(img, (5, 5))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
