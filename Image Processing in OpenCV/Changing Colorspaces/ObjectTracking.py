#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-16 21:21:26
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """
        蓝色的RGB颜色是0,0,255
        HSV颜色是120,255,255
        所以上限和下限为：
            [H - 10, 100, 100] --> [110,100,100]
            [H + 10, 255, 255] --> [130,255,255]
            如果想扩大范围，就修改上限为：[H - 10, 50, 50]
    """
    # define range of blue color in HSV
    lower_blue = np.array([20,100,100])
    upper_blue = np.array([40,255,255])

    """
        把一个BGR颜色转换为HSV颜色
        >>> green = np.uint8([[[0,255,0 ]]])
        >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        >>> print hsv_green
        [[[ 60 255 255]]]
        然后可以使用
            [H - 10, 100, 100]作为下限
            [H + 10, 255, 255]作为上限
    """


    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
