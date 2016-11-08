#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-08 20:57:19
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


cap = cv2.VideoCapture(0)

"""
    如果要传递MJPG，可以使用：
        cv2.VideoWriter_fourcc('M','J','P','G')
    或者：
        cv2.VideoWriter_fourcc(*'MJPG') 
"""
fourcc = cv2.VideoWriter_fourcc(*'XVID')
"""
    依次指定：
        文件名，
        视频编解码器的四字节代码，
        每秒的FPS，
        每一帧的大小
"""
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # 翻转每一帧
        frame = cv2.flip(frame, 0)

        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
