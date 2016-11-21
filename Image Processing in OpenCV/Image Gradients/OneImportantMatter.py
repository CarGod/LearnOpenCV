#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-21 23:10:06
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('box.png',0)

# Output dtype = cv2.CV_8U
# 只能检测一条边
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# 检测两条边需要保持输出类型为较高的形式如：cv2.CV_16S，cv2.CV_64F等
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# 取绝对值
abs_sobel64f = np.absolute(sobelx64f)
# 转换回cv2.CV_8U
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()
