#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 19:08:59
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    双边过滤
    在保持边缘清晰的同时在噪声去除方面非常有效。但是操作比其他过滤器慢
    模糊表面的纹理，但是边缘的还能够保存下来。
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('serrated.png')

"""
    参数一：接收的图像
    参数二：表面处理程度
    参数三四：x和y轴的模糊程度
"""
bilateral_blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(bilateral_blur), plt.title('Bilateral Blur')
plt.xticks([]), plt.yticks([])
plt.show()
