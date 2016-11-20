#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-20 23:01:55
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    我们的内核都是通过np.ones来构建的，这都是矩形的内核
    有时我们可能需要其他的内核，这时就需要手动构建
    # Rectangular Kernel
    >>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    array([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]], dtype=uint8)
    
    # Elliptical Kernel
    >>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    array([[0, 0, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [0, 0, 1, 0, 0]], dtype=uint8)
    
    # Cross-shaped Kernel
    >>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    array([[0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [0, 0, 1, 0, 0],
"""
