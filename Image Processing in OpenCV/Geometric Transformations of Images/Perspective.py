#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-18 21:38:03
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    透视转型
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../../GuiFeaturesinOpenCV/temp.jpg')
rows, cols, ch = img.shape

"""
    ptslist1 = [[56,65],[368,65],[56,387],[368,387]]
    ptslist2 = [[0,0],[300,0],[0,300],[300,300]]
    四个点中的任意三个点不应该是共线的
"""
ptslist1 = [[56,65],[368,52],[28,387],[389,390]]
ptslist2 = [[0,0],[300,0],[0,300],[300,300]]
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,255)]
count = 0

pts1 = np.float32(ptslist1)
pts2 = np.float32(ptslist2)

for list1 in ptslist1:
    x = list1[0]
    y = list1[1]
    cv2.circle(img,(x, y), 5, colors[count], -1)
    count+=1

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

db = dst[:,:,0]
dg = dst[:,:,1]
dr = dst[:,:,2]

img = cv2.merge((r,g,b))
dst = cv2.merge((dr,dg,db))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

