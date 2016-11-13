#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 17:30:21
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


def nothing(x):
    pass

img = np.zeros((300, 612, 3), np.uint8)
cv2.namedWindow('image')

"""
    第一个参数：
        拖动条的名称
    第二个参数：
        增加在哪个窗口
    第三第四个参数：
        最小值和最大值
    第五个参数：
        默认的回调函数，并且自带一个当前拖动条的值是多少
"""
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    """
        获取拖动条的值
            第一个参数：
                获取哪个名字的拖动条
            第二个参数：
                这个拖动条在哪个窗口
    """
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
