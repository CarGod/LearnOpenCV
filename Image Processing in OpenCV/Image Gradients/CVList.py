#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-21 22:56:48
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2


"""
    显示cv2里面深度参数都有哪些
"""
flags = [i for i in dir(cv2) if i.startswith('CV_')]
print(flags)
