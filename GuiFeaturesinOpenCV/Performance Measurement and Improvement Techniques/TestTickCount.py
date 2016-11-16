#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-15 21:31:30
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$


import numpy as np
import cv2


# 禁用后   1.4845137961317971 s
# 未禁用   1.2194205794521527 s
# cv2.setUseOptimized(False)
e1 = cv2.getTickCount()
print(e1)
for i in range(10000000):
    pass
e2 = cv2.getTickCount()
print(e2)
time = (e2 - e1) / cv2.getTickFrequency()
print(time)

print('=======================================')

img = cv2.imread('../temp.jpg', 0)

z = cv2.countNonZero(img)
print(z)

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img = cv2.medianBlur(img,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

"""
    许多OpenCV函数使用SSE2，AVX等进行优化，它也包含为优化的代码。
    在编译的时候默认是启用优化代码的，如果被禁用就会运行未优化的代码。
    下面的方法返回True则说明启用，False则是禁用，代码运行效率会变慢。
    使用cv2.setUseOptimized(False)方法可禁用
"""
print(cv2.useOptimized())

"""
    通常情况下，OpenCV的函数比Numpy的函数要更快，所以OpenCV的函数是首选的。
    当然也有例外的情况。
    In [1]: import cv2

    In [2]: import numpy as np

    In [3]: img = cv2.imread('temp.jpg')

    In [4]: %timeit z = cv2.countNonZero(img)
    The slowest run took 1370852.00 times longer than the fastest. This could mean that an intermediate result is being cached.
    1 loop, best of 3: 395 ns per loop

    In [5]: %timeit z = np.count_nonzero(img)
    The slowest run took 8194.78 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 612 ns per loop

    In [6]: %timeit z = np.count_nonzero(img)
    The slowest run took 13.04 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 606 ns per loop

    In [7]: %timeit z = cv2.countNonZero(img)
    The slowest run took 20.09 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 374 ns per loop
"""