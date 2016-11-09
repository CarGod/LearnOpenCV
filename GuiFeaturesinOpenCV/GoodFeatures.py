#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-09 21:16:51
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('temp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 25 是要寻找多少个点
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img),plt.show()