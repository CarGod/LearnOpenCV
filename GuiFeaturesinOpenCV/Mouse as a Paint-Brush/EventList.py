#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 12:31:58
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


event = [i for i in dir(cv2) if 'EVENT' in i]
print(event)
