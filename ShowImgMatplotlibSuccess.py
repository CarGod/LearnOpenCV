import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('temp.jpg')
b,g,r = cv2.split(img)
# 此时直接显示图片就是正常的了，下面只不过是为了对比多个模式而已
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()