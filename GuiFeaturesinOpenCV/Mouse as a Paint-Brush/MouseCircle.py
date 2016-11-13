#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 12:34:17
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2
import numpy as np

# mouse callback function
"""
    系统会传递过来：事件类型，x坐标和y坐标
    flags：
        0为没有按下鼠标任何键
        1为按下左键
        2为按下右键
        4为按下中健
    param:
        调用的时候可以传其他参数过来
"""
def draw_circle(event,x,y,flags,param):
    print(param)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, ' -- ', y)
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
# 显示一个新窗口
cv2.namedWindow('image')
# 给一个窗口绑定一个鼠标事件的回调函数，可以传递一个param过去
cv2.setMouseCallback('image',draw_circle, 'param')

while(1):
    # 在一个窗口上面显示图像
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
