#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-16 22:34:34
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


"""
    所有方法接受一个list返回一个list
"""
def bgr2hsv(bgr):
    bgr_uint8 = np.uint8([[bgr]])
    return cv2.cvtColor(bgr_uint8, cv2.COLOR_BGR2HSV)


def hsv2bgr(hsv):
    hsv_uint8 = np.uint8([[hsv]])
    return cv2.cvtColor(hsv_uint8, cv2.COLOR_HSV2BGR)


def rgb2hsv(rgb):
    rgb_uint8 = np.uint8([[rgb]])
    return cv2.cvtColor(rgb_uint8, cv2.COLOR_RGB2HSV)


def hsv2rgb(hsv):
    hsv_uint8 = np.uint8([[hsv]])
    return cv2.cvtColor(hsv_uint8, cv2.COLOR_HSV2RGB)


print(rgb2hsv([255,255,0]))
# print(rgb2hsv([255,200,200]))
# print(hsv2rgb([0,55,80]))

