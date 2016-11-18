#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-16 21:21:26
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


"""
    拉伸、收缩、扭曲、旋转是图像的几何变换，在三维视觉技术中大量应用到这些变换，
    又分为仿射变换和透视变换。仿射变换通常用单应性建模，利用cvWarpAffine解决密集
    映射，用cvTransform解决稀疏映射。仿射变换可以将矩形转换成平行四边形，它可以
    将矩形的边压扁但必须保持边是平行的，也可以将矩形旋转或者按比例变化。透视变换
    提供了更大的灵活性，一个透视变换可以将矩阵转变成梯形。当然，平行四边形也是梯
    形，所以仿射变换是透视变换的子集。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('../../GuiFeaturesinOpenCV/temp.jpg')
rows, cols, _ = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# 绘制仿射变换三角形
cv2.circle(img,(50,50), 5, (0,255,0), -1)
cv2.circle(img,(200,50), 5, (0,255,0), -1)
cv2.circle(img,(50,200), 5, (0,255,0), -1)
cv2.line(img, (50, 50), (200, 50), (255, 0, 0), 1)
cv2.line(img, (200, 50), (50, 200), (255, 0, 0), 1)
cv2.line(img, (50, 200), (50, 50), (255, 0, 0), 1)

"""
    系统根据两个三角形顶点之间的变幻规则，来确定图片变幻的样子

    pts1：
        仿射变换三角形原图三个顶点的位置
    pts2：
        仿射变换三角形变换后三个顶点的位置
"""
M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

db = dst[:,:,0]
dg = dst[:,:,1]
dr = dst[:,:,2]

img = cv2.merge((r,g,b))
dst = cv2.merge((dr,dg,db))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
