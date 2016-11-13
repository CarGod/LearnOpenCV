#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-12 22:43:16
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

"""
    line(img, start_site, end_site, bgr_color, line_size)
    img:
        图片的对象
    start_site:
        开始坐标(左，上)
    end_site:
        结束坐标(右，下)
    bgr_color:
        BGR的颜色
    line_size:
        画笔的宽度，-1代表填满，默认为1.
"""
cv2.line(img, (0, 0), (511,511), (255, 0, 0), 5)

"""
    矩形需要左上角，右下角的坐标
"""
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

"""
    圆需要指定中心点和半径
"""
cv2.circle(img,(447,63), 63, (0,0,255), -1)

"""
    ellipse：
        第一个参数：图片对象
        第二个参数：中心点的位置(x, y)
        第三个参数：(长轴的长度，短轴的长度)
        第四个参数：椭圆在顺时针方向旋转的角度
        第五第六个参数：中心点沿顺时针方向从x角度绘制到y角度。0, 360表示闭合图形
        第七个参数：表示颜色，255 = (255, 0, 0)
        第八个参数：表示线的宽度，-1为闭合图形填充满
"""
cv2.ellipse(img,(256,256),(100,50),0,0,180,(200, 200, 100),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1, 1, 2))
"""
    绘制多边形
    pts 是一个数组
    其中pst[0]表示多边形有多少个点，里面的每一个元素代表一个点的坐标
    pst[1]代表是int32类型的，这是必须的
    第三个参数如果设置为False就相当于单独绘制每一条线，而不会自动闭合
    这比调用四次cv2.line方法更好的绘制多条直线
"""
cv2.polylines(img, [pts], True, (0,255,255))


font = cv2.FONT_HERSHEY_SIMPLEX
"""
    第二个参数：要绘制的字体
    第三个参数：字体的左下角位置
    第四个参数：字体的样式
    第五个参数：字体的大小
    第六个参数：字体的颜色
    第七个参数：字体画笔的宽度
    第八个参数：画笔的类型，cv2.LINE_AA是推荐使用的，为了好看。
"""
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
