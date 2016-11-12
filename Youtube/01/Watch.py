#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-10 21:06:54
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2
from matplotlib import pyplot as plt

"""
IMREAD_GRAYSCALE    =   0
IMREAD_COLOR        =   1
IMREAD_UNCHANGED    =   -1
"""
img = cv2.imread('watch.png', 0)
# cv2.imshow('image', img)

plt.imshow(img, cmap='gray', interpolation='bicubic')
""" 
    [x1, x2] [y1, y2] 从x1, y1 画到 x2, y2
    第三个参数 'b' >> 'blue' 代表颜色首字母
    可以缩写，也可以写全
"""
plt.plot([100, 1400], [800, 0], 'blue', linewidth=10)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
