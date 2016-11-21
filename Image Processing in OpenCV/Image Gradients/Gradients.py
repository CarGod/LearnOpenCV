#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-21 22:20:27
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    边缘检测
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2



img = cv2.imread('dave.png', 0)


laplacian = cv2.Laplacian(img, cv2.CV_64F)

"""
    第一个参数：
        需要显示的图片
    第二个参数：
        输出图像的深度，可以使用-1
    第三个参数：
        1为显示垂直
    第四个参数：
        1为显示水平
    第五个参数：
        指定内核的大小，-1为3x3的内核
"""
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
