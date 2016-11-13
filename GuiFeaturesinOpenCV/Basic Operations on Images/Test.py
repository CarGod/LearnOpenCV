#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 21:44:39
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2
import numpy as np


def mouse_move(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x, y, flags, param)


img = cv2.imread('temp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
    读取一张BGR图片的Blue, Green, Red颜色的强度，返回一个list
    如果是一张灰度图片，则返回一个数字类型的强度
"""
px = img[100, 100]
px_gray = gray[100, 100]
print(px)
print(px_gray)

"""
    第三个参数表示返回数组的第几个元素
    这里表示只获取蓝色的强度
    相当于print(px[0])
"""
blue = img[100, 100, 0]
print(blue)

"""
    可以修改指定位置的颜色
"""
img[100, 100] = [255, 200, 100]
print(img[100, 100])


"""
    上面的方法，如果用来分别读取每一个像素点的颜色，并且去修改它。
    这样是效率非常低的，不推荐使用，应当使用更高级的方法。
    得到颜色：img.item()或修改颜色：img.itemset()，但是每次只能返回一个颜色的数值，所以
    如果想要得到BGR三个颜色，就要调用三个item方法。
"""
blue = img.item(100, 100, 0)
green = img.item(100, 100, 1)
red = img.item(100, 100, 2)
print([blue, green, red])

"""
    修改指定点的指定BGR中某一个的颜色
"""
img.itemset((100, 100, 0), 0)
print(img[100, 100])

"""
    img.shape属性可以用来：
        访问图片的，行数，列数，通道数
        返回一个元祖
"""
print(img.shape)

"""
    如果是灰度图片，只会返回行数和列数，而没有通道数
    所以这样是一个检测是否是一个灰度图片的很好的技巧
"""
print(gray.shape)

"""
    img.size 可以得到像素的总和
    彩色图片等于：行数x列数x通道数
"""
print(img.size)

"""
    灰度图片等于：行数x列数
"""
print(gray.size)

"""
    img.dtype可以获得图像的数据类型
    此属性在调试的时候非常重要，因为OpenCV很多错误
    都是由于无效的数据类型引起的
"""
print(img.dtype)
print(gray.dtype)

"""
    操作图像的选区，并且移动它
    读取坐标一般都是横坐标在前，竖坐标在后，正好相反。
    [竖线第一个点:竖线第二个点, 横线第一个点:横线第二个点]
"""
bun = img[249:326, 334:409]
"""
    移动的位置，必须符合原来截取图片的大小，否则就会报错。
"""
img[249-100:326-100, 334-100:409-100] = bun
# 取消下面代码的注释，可以看到图片的演示效果
# cv2.namedWindow('img')
# cv2.setMouseCallback('img', mouse_move)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
    有时我们需要单独使用BGR通道其中的一个来工作
    这时就需要用到拆分和合并图像的方法
    拆分：
        cv2.split(img) 方法返回三个参数b,g,r
    合并：
        cv2.merge((b,g,r)) 接收一个元组，内容是b,g,r
    cv2.split 是一个非常消耗性能的方法，除非真的需要。
    否则请使用numpy内置的，下标方式来操作这些行为。
"""
b,g,r = cv2.split(img)

"""
    如果想单独的获得其中的某一个
    b = img[:,:,0]就获得Blue
    这是numpy内置的，效率比cv2的更高。
"""
bx = img[:,:,0]
gx = img[:,:,1]
rx = img[:,:,2]
print('b ----\n{b}\ng ----\n{g}\nr ----\n{r}'.format(b=b, g=g, r=r))

"""
    如果想去掉红色的通道，可以简单的通过索引来操作
"""
img[:,:,2] = 0
# 取消注释可以看到效果
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()