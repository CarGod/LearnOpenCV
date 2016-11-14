#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-14 21:16:59
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


x = np.uint8([250])
y = np.uint8([10])

"""
    cv2的加法是一个饱和运算
    建议使用cv2的方法
    250 + 10 = 260 => 255
"""
print(cv2.add(x,y))

"""
    numpy的加法是一个模运算
    250 + 10 = 260 % 256 = 4
"""
print(x+y)
