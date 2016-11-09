import numpy as np
import cv2


# 打开摄像头，这里只有一个则使用第0个。
cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)

while True:
    # 逐帧的读取
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    dst = cv2.dilate(dst, None)

    frame[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow('dst', frame)
    
    # 如果按下q则退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有开启的窗口
cv2.destroyAllWindows()
