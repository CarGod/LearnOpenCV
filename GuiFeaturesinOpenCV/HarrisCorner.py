import numpy as np
import cv2


filename = 'temp.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

"""
	OpenCV的Harris角检测器
	cornerHarris(img, blockSize, ksize, k)
	接收四个参数。
	img:
		输入的图像，应该是灰度，float32的图像
	blockSize:
		角点检测时临近点的考虑大小，其实就是画出来的红点的大小
	ksize:
		使用的Sobel导数的孔径参数，这个好像必须用3。
	k:
		Harris检测器的自由参数，应该是检测的细致程度，越小检测的越入微。
"""
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()