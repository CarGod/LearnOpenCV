#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 21:30:18
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

from matplotlib import pyplot as plt
import numpy as np
import cv2


img = cv2.imread('j.png', 0)
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations = 1)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(dilation), plt.title('Dilation')
plt.show()
