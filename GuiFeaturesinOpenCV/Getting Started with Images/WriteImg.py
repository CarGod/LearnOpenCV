# -*- coding:utf-8 -*-


import numpy as np
import cv2

img = cv2.imread('temp.jpg', 0)
cv2.imshow('image', img)
# 如果是x64系统需要使用
#  ascii_key = cv2.waitKey(0) & 0xFF
ascii_key = cv2.waitKey(0)
if ascii_key == 27:
	# Esc 的 Ascii码为27
	cv2.destroyAllWindows()
elif ascii_key == ord('s'):
	# 如果按下的是s，就保存这个图片。
	cv2.imwrite('messigray.png', img)
	cv2.destroyWindow('image')
