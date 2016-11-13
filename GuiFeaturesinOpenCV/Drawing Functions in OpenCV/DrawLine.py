#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-12 22:34:12
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2


img = np.zeros((512, 512, 3), np.uint8)



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
