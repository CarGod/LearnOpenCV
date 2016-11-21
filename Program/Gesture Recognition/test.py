#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 19:08:59
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


from matplotlib import pyplot as plt
import numpy as np
import cv2


# 获取第一个摄像头
cap = cv2.VideoCapture(0)

# 设置宽高
# cap.set(3, 1024)
# cap.set(4, 768)

while True:
    # 读取当前摄像头看到的图像
    ret, frame = cap.read()


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
    lower_blue = np.array([50,100,100])
    upper_blue = np.array([70,255,255])

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

    # cv2.imshow('Gesture Recognition V 0.0.1',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    # 每隔一秒刷新一次图像，检测是不是按下q键退出
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭开启的窗口
cv2.destroyAllWindows()

