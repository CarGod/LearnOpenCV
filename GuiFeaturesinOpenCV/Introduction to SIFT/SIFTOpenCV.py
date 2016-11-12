#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-09 21:59:26
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2
import numpy as np

img = cv2.imread('temp.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

"""
    如果报出无法找到xfeatures2d，是因为OpenCV在3.x中，把这个
    模块移动到了contrib中，并且作为一个单独的项目安装。
    所以，在安装OpenCV的时候需要安装：(以3.1.0版本为例)
    opencv_python-3.1.0+contrib_opencl-cp35-cp35m-win_amd64
"""
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp,img)

cv2.imwrite('sift_keypoints.jpg',img)