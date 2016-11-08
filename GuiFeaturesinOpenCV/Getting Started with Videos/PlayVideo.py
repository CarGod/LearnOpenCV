#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-08 19:59:24
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


cap = cv2.VideoCapture('video.flv')

# 判断视频是否到了尽头
while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    """
        此处，如果waitKey里面的数值越小，视频播放就越快
        相反，数值越大，视频播放就越慢，这可以用来慢动作播放视频
        正常情况下设置为25毫秒是最合理的
    """
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
