# -*- coding:utf-8 -*-

import numpy as np
import cv2


"""
	读取一张图片
	imread(image_path, load_type)
	image_path: 
		读取图片的路径。
	load_type：
		读取图片的方式-1,0,1
		cv2.IMREAD_COLOR : -1, 默认行为。彩色模式加载图像，忽略透明度。
		cv2.IMREAD_GRAYSCALE : 0，灰度模式加载。
		cv2.IMREAD_UNCHANGED : 1，加载图像，包括alpha通道。
		如果想以灰度模式打开，可以传递cv2.IMREAD_GRAYSCALE，也可以使用简单的0。
"""
img = cv2.imread('c:\\open\\temp.jpg', 0)

"""
	使用一个窗口显示图片，窗口的大小自适应图片。
	imshow(window_name, image_obj)
	window_name:
		显示窗口的名称
	image_obj:
		读取出来的图片对象
"""
cv2.imshow('This is a image.', img)

"""
	多少毫秒后自动退出程序，或在多少毫秒内，按任意键退出。
	0 为永远等待按下任意键退出，并且该函数还处理许多其他GUI的事件。
	所以，图像的加载实际上是依赖于该函数的，如果不执行该函数，图像不会
	被加载，只会加载一个空的窗口。
"""
cv2.waitKey(0)
"""
	销毁所有创建的窗口。
	如果要销毁某一个窗口则需要使用cv2.destroyWindow()，
	并传递一个窗口名称作为参数。
"""
cv2.destroyAllWindows()

# --------------------------一条华丽的分割线-------------------------------------

"""
	创建一个可调整大小的窗口
	namedWindow(window_name, type)
	window_name:
		窗口名称
	type:
		cv2.WINDOW_AUTOSIZE：图片默认的大小
		cv2.WINDOW_NORMAL：可调整窗口的大小，并且图片的大小随窗口的改变而改变
"""
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
