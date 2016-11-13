#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 17:04:08
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-13 16:50:38
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                img2 = np.zeros((768, 1024,4), np.uint8)
                cv2.rectangle(img2,(ix,iy),(x,y),(0,255,0),1)
                cv2.imshow('image',img2)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

# zeros(高, 宽, 通道数量[1, 3, 4])
img = np.zeros((768, 1024,4), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    if k == ord('c'):
        cv2.rectangle(img,(0,0),(1024,768),(0,0,0),-1)
    elif k == 27:
        break

cv2.destroyAllWindows()


