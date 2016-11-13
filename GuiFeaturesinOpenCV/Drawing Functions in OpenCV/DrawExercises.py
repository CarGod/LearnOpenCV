#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 11:53:21
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


img = np.zeros((512, 512, 3), np.uint8)

# R:255 G:0 B:0
# 
# B:0 G:0 R:255
cv2.ellipse(img,(256,210),(50,50),135,0,270,(0, 0, 255),30)

cv2.imshow('Exeprcises', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
