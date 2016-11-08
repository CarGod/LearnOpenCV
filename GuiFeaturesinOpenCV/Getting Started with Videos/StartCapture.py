import numpy as np
import cv2


# 打开摄像头，这里只有一个则使用第0个。
cap = cv2.VideoCapture(0)

"""
    cap.get(propId)
    cap.set(propId, value)
    propId 想要获得或设置内容的ID，从1到18。
    3：宽度
    4：高度
    如：
        设置高度和宽度从320x240到640x480。
        ret = cap.set(3, 640)
        ret = cap.set(4. 480)
"""
cap.set(3, 1024)
cap.set(4, 768)

while True:
    # 逐帧的读取
    ret, frame = cap.read()

    # 设置使用灰度模式来渲染
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示图像
    cv2.imshow('frame', gray)
    
    # 如果按下q则退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有开启的窗口
cv2.destroyAllWindows()
