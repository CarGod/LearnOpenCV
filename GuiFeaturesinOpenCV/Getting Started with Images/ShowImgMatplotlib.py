"""
	Anaconda 更换国内的源
	pipy国内镜像目前有：
	 
	http://pypi.douban.com/  豆瓣
	http://pypi.hustunique.com/  华中理工大学
	http://pypi.sdutlinux.org/  山东理工大学
	http://pypi.mirrors.ustc.edu.cn/  中国科学技术大学
	注意后面要有/simple目录！！！
	更新一下：
	确实add channel的时候不用加引号
	另外答主没有提怎么删除原来加错的channel，我搜了一下，配置文件是.condarc，可以通过conda info -a命令查看路径C:UsersAdministrator.condarc。通过记事本直接打开，把默认的和加错的都删掉，只留一个对的就行了。
	-----以下是原始记录，因为手机上没法编辑问题，只好把补充说明写在这里了-----------

	conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'

	conda config --set show_channel_urls yes
	加了上面的源，但并没有使用。
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

"""
	这里使用灰度模式就没有问题，如果使用1就会出现问题
	原因是因为，OpenCV使用的是，BGR模式，而Matplotlib
	使用的是RGB模式显示的。
	解决方法：
	http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748
"""
img = cv2.imread('temp.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()