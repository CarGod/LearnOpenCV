#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-16 20:52:04
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2


"""
    显示cv2里面颜色转换的参数有哪些
"""
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)